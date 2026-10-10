-- Removes RevealJS pause markers (". . ." paragraphs) from every output format
-- except revealjs, where Pandoc turns them into fragment breaks. Without this
-- filter the markers show up as literal ". . ." text on the HTML lecture pages,
-- in the Typst PDF and in the hugo-md output.
if quarto.doc.is_format("revealjs") then
  return {}
end

return {
  {
    Para = function(el)
      if pandoc.utils.stringify(el) == ". . ." then
        return {}
      end
    end
  }
}
