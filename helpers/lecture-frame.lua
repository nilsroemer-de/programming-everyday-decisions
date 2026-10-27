-- Lecture frame: "say what you're going to say, say it, say what you said".
--
-- Reads five metadata fields from the lecture's YAML header
--   lecture-summary   one sentence
--   lecture-why       short paragraph
--   lecture-roadmap   list of exactly three points (= titles of the three sections)
--   lecture-covered   list of three sentences, one per roadmap point
--   lecture-key       key message
-- and generates from them
--   revealjs: "Today in one sentence" (summary + why), "Roadmap", then the content of
--             section 1 directly; sections 2 and 3 start with one roadmap slide (current
--             point highlighted) that replaces the section title slide; a short slide
--             with the covered sentence at the end of every section, and the closing slides
--             "What we covered", "Why it matters" and the key message. The closing
--             slides replace an empty div `::: {.lecture-closing}` in the source.
--   other formats (HTML page, PDF, md): summary, why and roadmap as text at the top,
--             "What we covered" and the key message at the closing marker; speaker
--             notes (`::: {.notes}`) become a visible "Notes" block on the HTML page
--             and are dropped in PDF and md.
-- A lecture without lecture-roadmap is left untouched.

local stringify = pandoc.utils.stringify

local function as_inlines(v)
  local t = pandoc.utils.type(v)
  if t == "Inlines" then return v end
  if t == "Blocks" then return pandoc.utils.blocks_to_inlines(v) end
  if t == "string" then return pandoc.Inlines(pandoc.Str(v)) end
  return pandoc.Inlines(pandoc.Str(stringify(v)))
end

local function as_list(v)
  local out = {}
  if v == nil then return out end
  if pandoc.utils.type(v) == "List" then
    for _, item in ipairs(v) do table.insert(out, as_inlines(item)) end
  else
    table.insert(out, as_inlines(v))
  end
  return out
end

local function norm(s)
  return (stringify(s):lower():gsub("%s+", " "):gsub("^%s", ""):gsub("%s$", ""))
end

local function eyebrow(text)
  return pandoc.Para({ pandoc.Span(pandoc.Inlines(pandoc.Str(text)), { class = "eyebrow" }) })
end

local function roadmap_block(points, current)
  local items = {}
  for i, p in ipairs(points) do
    local cls = "future"
    if current then
      if i == current then cls = "current" elseif i < current then cls = "done" end
    end
    table.insert(items, { pandoc.Plain({ pandoc.Span(p, { class = "roadmap-item " .. cls }) }) })
  end
  return pandoc.Div({ pandoc.OrderedList(items) }, { class = "roadmap" })
end

local function statement(inl, cls)
  return pandoc.Para({ pandoc.Span(inl, { class = cls or "statement" }) })
end

-- Split the key message at sentence ends so each sentence fits on its own line.
local function key_lines(inl)
  local text = stringify(inl)
  local lines = {}
  for sentence in text:gmatch("[^%.!?]+[%.!?]*") do
    local s = sentence:gsub("^%s+", ""):gsub("%s+$", "")
    if s ~= "" then table.insert(lines, pandoc.Para({ pandoc.Str(s) })) end
  end
  if #lines == 0 then lines = { pandoc.Para(inl) } end
  return lines
end

function Pandoc(doc)
  local meta = doc.meta
  if meta["lecture-roadmap"] == nil then return nil end

  local summary = as_inlines(meta["lecture-summary"] or "")
  local why = as_inlines(meta["lecture-why"] or "")
  local roadmap = as_list(meta["lecture-roadmap"])
  local covered = as_list(meta["lecture-covered"])
  local key = as_inlines(meta["lecture-key"] or "")
  if #roadmap ~= 3 then
    quarto.log.warning("lecture-frame: lecture-roadmap must have exactly 3 points, found " .. #roadmap)
  end
  if #covered ~= #roadmap then
    quarto.log.warning("lecture-frame: lecture-covered must have one sentence per roadmap point")
  end

  local reveal = quarto.doc.is_format("revealjs")
  local html = quarto.doc.is_format("html")
  local blocks = pandoc.List()

  -- opening -------------------------------------------------------------
  if reveal then
    blocks:insert(pandoc.Header(2, pandoc.Inlines(pandoc.Str("Today in one sentence")), { class = "lecture-opening" }))
    blocks:insert(pandoc.Div({ statement(summary) }, { class = "lecture-summary" }))
    blocks:insert(pandoc.Div({ eyebrow("Why it matters"), pandoc.Para(why) }, { class = "lecture-why" }))
    blocks:insert(pandoc.Header(2, pandoc.Inlines(pandoc.Str("Roadmap")), { class = "lecture-opening" }))
    blocks:insert(roadmap_block(roadmap, nil))
  else
    local intro = pandoc.List()
    intro:insert(pandoc.Para({ pandoc.Strong(summary) }))
    intro:insert(pandoc.Para(why))
    intro:insert(pandoc.Para({ pandoc.Strong(pandoc.Inlines(pandoc.Str("Roadmap")))}))
    intro:insert(roadmap_block(roadmap, nil))
    blocks:insert(pandoc.Div(intro, { class = "lecture-intro" }))
  end

  -- body ---------------------------------------------------------------
  local current = nil
  local seen = {}

  local function covered_slide(i)
    if not reveal or covered[i] == nil then return end
    blocks:insert(pandoc.Header(2, roadmap[i], { class = "section-covered" }))
    blocks:insert(pandoc.Div({ eyebrow("What we covered"), statement(covered[i]) }, { class = "section-covered" }))
  end

  local function closing()
    if reveal then
      blocks:insert(pandoc.Header(2, pandoc.Inlines(pandoc.Str("What we covered")), { class = "lecture-closing" }))
      local items = pandoc.List()
      for i, p in ipairs(roadmap) do
        items:insert(pandoc.Div({ eyebrow(stringify(p)), pandoc.Para(covered[i] or pandoc.Inlines{}) }, { class = "covered-item" }))
      end
      blocks:insert(pandoc.Div(items, { class = "covered-list" }))
      blocks:insert(pandoc.Header(2, pandoc.Inlines(pandoc.Str("Why it matters")), { class = "lecture-closing" }))
      blocks:insert(pandoc.Div({ pandoc.Para(why) }, { class = "lecture-why closing" }))
      blocks:insert(pandoc.Header(2, pandoc.Inlines{}, { class = "loud-slide lecture-key" }))
      blocks:insert(pandoc.Div(key_lines(key), { class = "r-fit-text" }))
    else
      blocks:insert(pandoc.Header(2, pandoc.Inlines(pandoc.Str("What we covered")), { class = "lecture-closing" }))
      local items = {}
      for i, p in ipairs(roadmap) do
        table.insert(items, { pandoc.Para({ pandoc.Strong(p), pandoc.Str(":"), pandoc.Space() } .. (covered[i] or pandoc.Inlines{})) })
      end
      blocks:insert(pandoc.BulletList(items))
      blocks:insert(pandoc.Para({ pandoc.Strong(key) }))
    end
  end

  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" and b.level == 1 then
      local n = norm(b.content)
      local idx = nil
      for i, p in ipairs(roadmap) do
        if norm(p) == n then idx = i end
      end
      if idx then
        if current then covered_slide(current) end
        current = idx
        seen[idx] = true
        if reveal then
          -- Section 1 follows the opening roadmap directly; sections 2 and 3 get one
          -- roadmap slide with the current point highlighted instead of a title slide.
          if idx > 1 then
            blocks:insert(pandoc.Header(2, pandoc.Inlines(pandoc.Str("Roadmap")), { class = "section-roadmap" }))
            blocks:insert(roadmap_block(roadmap, idx))
          end
        else
          blocks:insert(b)
        end
      else
        blocks:insert(b)
      end
    elseif b.t == "Div" and b.classes:includes("lecture-closing") then
      if current then covered_slide(current) end
      current = nil
      closing()
    elseif b.t == "Div" and b.classes:includes("notes") and not reveal then
      if html then
        local inner = pandoc.List({ eyebrow("Notes") })
        inner:extend(b.content)
        blocks:insert(pandoc.Div(inner, { class = "lecture-notes" }))
      end
      -- dropped in pdf / md
    else
      blocks:insert(b)
    end
  end

  for i, p in ipairs(roadmap) do
    if not seen[i] then
      quarto.log.warning("lecture-frame: no section header matches roadmap point " .. i .. ": " .. stringify(p))
    end
  end

  doc.blocks = blocks
  return doc
end
