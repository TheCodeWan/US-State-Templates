# US-State-Templates

This repository provides ready-to-use maps of the United States in two forms:

- **Editable HTML templates** (built with SVG) — you can easily recolor individual states by editing simple CSS.
- **High-resolution PNG images** — ready-to-use pictures for documents, slides, websites, or print.

## Why We Make Both HTML and PNG Versions

We maintain both versions for different needs:

- The **HTML files** are templates. Anyone can open them in a text editor (or browser) and change the color of any state instantly by editing a few lines of CSS. This is perfect for data visualizations, political maps, or any time you need to customize which states are highlighted.
- The **PNG files** are the finished, high-quality images. They are rendered at 4× resolution so they stay sharp even when scaled up. They have a clean white background so they work reliably in any context (including dark mode or when placed over other backgrounds).

In short: edit the HTML when you want to customize, use the PNG when you just need the final image.

## How to Turn an HTML Map into a PNG Image

Making the PNG from the HTML is simple:

1. Edit the `.html` file (change colors using the CSS rules inside the `<defs><style>` section of the SVG).
2. From the root of this repository, run:

```bash
python scripts/generate-pngs.py --file "path/to/the/file.html"
```

The script will:
- Pull out the SVG from the HTML
- Make sure it has a solid white background
- Render it at exactly 4× size (4076 × 3888 pixels)
- Save the PNG right next to the HTML file

That's all you need to do.

Here is an example of the **colored map**:

![US States Colored Example](Maps%20of%20the%20entire%20US/examples/colored/us-states-colored.png)

Here is the basic **labeled template**:

![US States Labeled Template](Maps%20of%20the%20entire%20US/templates/labeled/us-states-labeled.png)

## Repository Structure

```
Maps of the entire US/
├── examples/
│   ├── colored/                    # Example with multiple colors
│   ├── concealed-carry-sd/         # Example showing South Dakota gun permit reciprocity
│   └── state-government-trifectas/ # State government trifectas
└── templates/
    ├── blank/                      # Blank (unlabeled) template
    └── labeled/                    # Basic labeled template
```

Each folder contains a matching pair:
- `us-states-*.html` — the editable SVG map
- `us-states-*.png` — the high-resolution (4×) preview image

## Generating PNGs from HTML

(For full details and options, see the section above.)

Quick commands:

```bash
# Regenerate all PNGs
python scripts/generate-pngs.py

# Regenerate one file
python scripts/generate-pngs.py --file "Maps of the entire US/templates/labeled/us-states-labeled.html"

# Check that PNGs are up to date
python scripts/generate-pngs.py --check
```

## Contributing

1. Edit the `.html` file.
2. Run the generation script for that file.
3. Commit both the `.html` and the new `.png`.
4. Open a pull request.

A GitHub Action will automatically check that the PNG matches the HTML.

## Notes

- All maps use the same canvas size (`width="1019" height="972"`, `viewBox="-30 -74 1019 972"`).
- PNGs are rendered at 4× scale for crisp results.
- Callout lines for small states (DE, RI, DC) are built into the SVG.

