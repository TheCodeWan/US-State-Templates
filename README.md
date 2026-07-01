# US-State-Templates

This repository contains a collection of map templates for the United States.

The maps come in two forms:

- **HTML files** — These are interactive editable SVG maps. You can open them in a web browser, or edit them with any text editor to change which states are highlighted or what colors they use.
- **PNG images** — High-resolution versions of the maps that are ready to drop into documents, slides, or websites.

## Template Example

Here is the basic labeled template:

![US States Labeled Template](Maps%20of%20the%20entire%20US/templates/labeled/us-states-labeled.png)

## Colored Example

Here is an example of a colored version of the map:

![US States Colored Example](Maps%20of%20the%20entire%20US/examples/colored/us-states-colored.png)

## Repository Structure

```
Maps of the entire US/
├── templates/
│   ├── blank/                      # Blank (unlabeled) template
│   └── labeled/                    # Basic labeled template
└── examples/
    ├── colored/                    # Example with multiple colors
    ├── concealed-carry-sd/         # Example showing South Dakota gun permit reciprocity
    └── state-government-trifectas/ # State government trifectas
```

Each folder contains a matching pair:
- `us-states-*.html` — the editable SVG map
- `us-states-*.png` — the high-resolution (4×) preview image

## How to Generate PNG Images from the HTML Files

When you edit one of the HTML map files (for example, to highlight different states), you will want to create an updated PNG image.

### On a Mac

1. Open the **Terminal** app.  
   You can do this by pressing `Command + Space`, typing "Terminal", and hitting Enter.

2. Navigate to the folder that contains this repository (this is called the "root" of the repository).

   For example, if you cloned or downloaded the repository to your Desktop and it is named `US-State-Templates`, you would type this and press Enter:

   ```bash
   cd ~/Desktop/US-State-Templates
   ```

   (If your folder is in a different location, adjust the path accordingly.)

3. Make sure you have the required tool installed:

   ```bash
   brew install librsvg
   ```

4. Run the generation script. Replace the path in the command with the HTML file you edited.

   Example for the labeled template:

   ```bash
   python png-generator/generate-pngs.py --file "Maps of the entire US/templates/labeled/us-states-labeled.html"
   ```

   The script will create or update the matching PNG file next to the HTML file.

That's all you need to do. The script handles extracting the map and rendering it at high resolution with a clean white background.

For reference, here are the most common commands:

```bash
# Generate PNGs for every map
python png-generator/generate-pngs.py

# Generate PNG for one specific file
python png-generator/generate-pngs.py --file "Maps of the entire US/templates/labeled/us-states-labeled.html"

# Check if the PNGs are up to date with the HTML files
python png-generator/generate-pngs.py --check
```

## Contributing

1. Edit the `.html` file.
2. Run the generation script to update the corresponding `.png`.
3. Commit both the HTML and PNG.
4. Open a pull request.

A GitHub Action will check that the PNGs are up to date.

## Notes

- All maps use the same canvas size.
- PNGs are rendered at 4× resolution (4076 × 3888 pixels) so they look sharp.
- The callout lines for small states (like DE, RI, and DC) are part of the SVG.

