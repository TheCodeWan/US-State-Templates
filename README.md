# US-State-Templates

This repository contains high-quality SVG-based HTML map templates and pre-rendered PNG images for the United States.

Each map is designed so that individual states (or groups of states) can be easily colored by editing simple CSS classes inside the HTML.

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

When you edit an `.html` map, you should regenerate the corresponding `.png` so the preview stays in sync.

### Prerequisites

You need `rsvg-convert` from librsvg:

- **macOS**  
  ```bash
  brew install librsvg
  ```

- **Ubuntu / Debian**  
  ```bash
  sudo apt update
  sudo apt install librsvg2-bin
  ```

- **Windows**  
  Use WSL and install via `apt`, or install via MSYS2.

Python 3 is also required (standard on modern macOS and Linux).

### Usage

From the root of the repository:

```bash
# Regenerate PNGs for every map in the repository
python scripts/generate-pngs.py

# Regenerate only one specific map
python scripts/generate-pngs.py --file "Maps of the entire US/templates/labeled/us-states-labeled.html"

# Verify that all PNGs are up to date (useful in CI or before committing)
python scripts/generate-pngs.py --check
```

The script will:
- Extract the SVG from the HTML file
- Ensure a white background (so it looks correct in dark mode)
- Render at exactly 4× resolution (4076 × 3888 pixels)
- Write the PNG next to the HTML file

### Continuous Integration

A GitHub Action (`.github/workflows/check-pngs.yml`) automatically runs `--check` on pull requests that modify any `.html` file under `Maps of the entire US/`. If a PNG is out of date, the check will fail.

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
- The callout lines (pointers for small states like DE, RI, DC) are part of the SVG and will render correctly as long as the CSS rules for `.label` and `.callout-line` exist inside the SVG's `<defs><style>` block.
