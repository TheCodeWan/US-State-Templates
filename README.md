# US-State-Templates

This repository provides ready-to-use maps of the United States in two forms:

- **Editable HTML templates** (built with SVG) — you can easily recolor individual states by editing simple CSS.
- **High-resolution PNG images** — ready-to-use pictures for documents, slides, websites, or print.

## Converting HTML Templates to PNG Images

When you customize one of the HTML map files, you need to generate a matching PNG image.

Here is the process and the reasoning behind each step:

1. **Edit the HTML file**  
   Change the colors of states by editing the CSS rules inside the `<defs><style>` section of the SVG. The HTML files are designed so that each state has its own class (like `.al`, `.ca`, etc.) that you can target.

2. **Run the generation script**  
   From the root of the repository, use:

   ```bash
   python scripts/generate-pngs.py --file "path/to/your-file.html"
   ```

   **Why we do it this way:**

   - We extract only the `<svg>` content from the HTML file. The surrounding HTML (body styles, centering div, etc.) is only there to make the map look nice when opened directly in a browser. For the final image we only need the vector graphic itself.
   - We automatically insert a white background rectangle. The raw SVG has no background by default. Adding one ensures the PNG always has a clean, solid white background no matter where it is used.
   - We render at exactly 4× the size declared in the SVG (`width="1019" height="972"` becomes 4076 × 3888 pixels). This matches the resolution used for all the other maps in the repository and produces crisp results.
   - We use `rsvg-convert` (from librsvg) because it produces high-quality, accurate rasterizations of the SVG and respects the exact viewBox and dimensions we need.

Here is the basic **labeled template**:

![US States Labeled Template](Maps%20of%20the%20entire%20US/templates/labeled/us-states-labeled.png)

Here is the **colored example**:

![US States Colored Example](Maps%20of%20the%20entire%20US/examples/colored/us-states-colored.png)

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

For full details and options, see the section above.

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

1. Edit the `.html` file you want to change (colors, labels, titles, keys, etc.).
2. Run the generation script to update the PNG:
   ```bash
   python scripts/generate-pngs.py --file "path/to/your-file.html"
   ```
3. Commit both the `.html` and the updated `.png`.
4. Open a pull request.

The CI will verify that the PNG matches the HTML.

## Notes

- All maps use the same canvas size (`width="1019" height="972"`, `viewBox="-30 -74 1019 972"`).
- PNGs are always generated at 4× scale for crisp display.
- The callout lines (pointers for small states like DE, RI, DC) are built into the SVG and will render correctly as long as the CSS rules for `.label` and `.callout-line` exist inside the SVG's `<defs><style>` block.
