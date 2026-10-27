-- Speaker notes (::: {.notes}) outside RevealJS: on the HTML lecture page they become a
-- visible "Notes" block (class lecture-notes, styled in styles.scss); in the Typst PDF and
-- the md export they are dropped. In RevealJS Quarto handles them as speaker notes.
if quarto.doc.is_format("revealjs") then
  return {}
end

local html = quarto.doc.is_format("html")

return {
  {
    Div = function(el)
      if not el.classes:includes("notes") then return nil end
      if not html then return {} end
      local inner = pandoc.List({ pandoc.Para({ pandoc.Span(pandoc.Inlines(pandoc.Str("Notes")), { class = "eyebrow" }) }) })
      inner:extend(el.content)
      return pandoc.Div(inner, { class = "lecture-notes" })
    end
  }
}
