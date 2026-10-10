// Typst template partial for the course PDFs (registered in _quarto.yml under
// format.typst.template-partials). Based on Quarto's default
// `typst-template.typ`; changed: left-aligned title block in the style of the
// website page header (title in Poppins, subtitle and Lecturer/Affiliation as
// muted Space Mono labels), quieter headings, code blocks and spacing.
// Fonts, colours and code background come from _brand.yml via Quarto.

#let course-ink = rgb("#1e2648")
#let course-primary = rgb("#01579b")
#let course-fg-2 = rgb("#4a5578")
#let course-fg-3 = rgb("#8a93ad")
#let course-border = rgb("#dde5ee")
#let course-sky-100 = rgb("#f3f8fd")

#let article(
  title: none,
  subtitle: none,
  authors: none,
  keywords: (),
  date: none,
  abstract-title: none,
  abstract: none,
  thanks: none,
  cols: 1,
  lang: "en",
  region: "US",
  font: none,
  fontsize: 11pt,
  title-size: 1.5em,
  subtitle-size: 1.25em,
  heading-family: none,
  heading-weight: "bold",
  heading-style: "normal",
  heading-color: black,
  heading-line-height: 0.65em,
  mathfont: none,
  codefont: none,
  linestretch: 1,
  sectionnumbering: none,
  linkcolor: none,
  citecolor: none,
  filecolor: none,
  toc: false,
  toc_title: none,
  toc_depth: none,
  toc_indent: 1.5em,
  doc,
) = {
  // Set document metadata for PDF accessibility
  set document(title: title, keywords: keywords)
  set document(
    author: authors.map(author => content-to-string(author.name)).join(", ", last: " & "),
  ) if authors != none and authors != ()
  set par(
    justify: false,
    leading: linestretch * 0.7em,
    spacing: 1.1em,
  )
  set text(lang: lang,
           region: region,
           size: fontsize)
  set text(font: font) if font != none
  show math.equation: set text(font: mathfont) if mathfont != none
  show raw: set text(font: codefont) if codefont != none

  set heading(numbering: sectionnumbering)

  show link: set text(fill: rgb(content-to-string(linkcolor))) if linkcolor != none
  show ref: set text(fill: rgb(content-to-string(citecolor))) if citecolor != none
  show link: this => {
    if filecolor != none and type(this.dest) == label {
      text(this, fill: rgb(content-to-string(filecolor)))
    } else {
      text(this)
    }
   }

  // Headings: no numbering, generous space above, little below (website page header rule)
  show heading.where(level: 1): it => block(above: 2.2em, below: 0.8em)[
    #set text(size: 15pt)
    #it.body
  ]
  show heading.where(level: 2): it => block(above: 1.8em, below: 0.6em)[
    #set text(size: 12.5pt)
    #it.body
  ]
  show heading.where(level: 3): it => block(above: 1.4em, below: 0.5em)[
    #set text(size: 11pt)
    #it.body
  ]
  show heading.where(level: 4): it => block(above: 1.2em, below: 0.4em)[
    #set text(size: 10.5pt)
    #it.body
  ]

  // Code blocks: light sky panel with a faint border, small Space Mono
  show raw.where(block: true): set block(inset: 9pt, radius: 4pt, width: 100%, stroke: 0.5pt + course-border)
  show raw.where(block: true): set text(size: 8.5pt)
  show raw.where(block: false): set text(size: 0.9em)

  // Lists: muted markers, a little air between items
  set list(marker: text(fill: course-fg-3)[•], spacing: 0.7em)
  set enum(spacing: 0.7em)

  // Page footer: page number as a small Space Mono label
  set page(footer: context [
    #set align(center)
    #set text(font: ("Space Mono",), size: 7.5pt, fill: course-fg-3)
    #counter(page).display("1")
  ])

  let has-title-block = title != none or (authors != none and authors != ()) or date != none or abstract != none
  if has-title-block {
    block(below: 2.2em, width: 100%)[
      #set align(left)
      #if title != none {
        block(below: 1.2em)[
          #set par(leading: 0.35em)
          #set text(font: heading-family) if heading-family != none
          #set text(weight: heading-weight)
          #set text(style: heading-style) if heading-style != "normal"
          #set text(fill: heading-color) if heading-color != black
          #text(size: 22pt)[#title #if thanks != none {
            footnote(thanks, numbering: "*")
            counter(footnote).update(n => n - 1)
          }]
        ]
      }
      #if subtitle != none {
        block(below: 1.6em)[
          #text(font: ("Space Mono",), size: 8.5pt, fill: course-fg-3)[#subtitle]
        ]
      }
      #if authors != none and authors != () {
        let label(t) = text(font: ("Poppins",), size: 6.5pt, weight: 700, tracking: 0.14em, fill: course-fg-3)[#upper(t)]
        let meta(t) = text(font: ("Space Mono",), size: 8.5pt, fill: course-fg-2)[#t]
        for author in authors {
          grid(
            columns: (auto, auto),
            column-gutter: 3em,
            row-gutter: 0.45em,
            label("Lecturer"), if author.affiliation != [] { label("Affiliation") } else { [] },
            meta(author.name), if author.affiliation != [] { meta(author.affiliation) } else { [] },
          )
        }
      }
      #if date != none {
        block(above: 1em)[#text(font: ("Space Mono",), size: 8.5pt, fill: course-fg-3)[#date]]
      }
      #if abstract != none {
        block(above: 1.5em)[
          #text(weight: "semibold")[#abstract-title] #h(1em) #abstract
        ]
      }
    ]
  }

  if toc {
    let title = if toc_title == none {
      auto
    } else {
      toc_title
    }
    block(above: 0em, below: 2em)[
    #outline(
      title: toc_title,
      depth: toc_depth,
      indent: toc_indent
    );
    ]
  }

  doc
}

#set table(
  inset: 6pt,
  stroke: none
)
