### DEPRECATED, use generate_icons.py instead
###generate black and white logo files

import os
from pathlib import Path
from cairosvg import svg2png
from PIL import Image
import io

# --- Configuration for Favicon PNGs ---
# The SVG content for your RV logo (for favicons)
# These will pick up colors from the theme (currentColor)
RV_SVG_CONTENT_FAVICON = r"""
<svg id="logo" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 100 100">
  <title>Logo</title>
  <g transform="translate(10, 5)">
    
    <polygon
      id="Shape"
      stroke="currentColor"
      stroke-width="4"
      fill="none"
      stroke-linecap="round"
      stroke-linejoin="round"
      points="40 0, 80 22.5, 80 67.5, 40 90, 0 67.5, 0 22.5"
    />
    
    <g transform="translate(12, 26) scale(0.7)">
      <path d="M 65.7 53.325 L 57.675 53.325 L 38.4 2.7 L 45.375 0 L 61.875 45.525 L 78.45 0.225 L 84.9 2.7 L 65.7 53.325 Z M 37.275 51.075 L 30.6 54.225 L 24.075 39.975 Q 21.6 34.65 17.85 32.4 A 17.9 17.9 0 0 0 8.973 30.159 A 29.414 29.414 0 0 0 8.25 30.15 L 7.125 30.15 L 7.125 53.325 L 0 53.325 L 0 0.975 Q 3.975 0.6 7.612 0.412 Q 11.25 0.225 15.375 0.225 A 30.934 30.934 0 0 1 24.668 1.459 A 15.622 15.622 0 0 1 29.812 4.125 Q 34.65 8.025 34.65 14.175 Q 34.65 19.65 31.387 22.987 A 19.111 19.111 0 0 1 23.286 27.594 A 32.096 32.096 0 0 1 21.975 27.975 Q 24 28.875 25.575 30.112 Q 27.15 31.35 28.612 33.412 Q 30.075 35.475 31.575 38.775 L 37.275 51.075 Z M 7.125 6.525 L 7.125 24.15 L 15.375 24.15 Q 20.775 24.15 24.15 21.75 Q 27.525 19.35 27.525 14.85 Q 27.525 11.1 24.375 8.662 A 13.099 13.099 0 0 0 17.137 6.285 A 25.193 25.193 0 0 0 15.375 6.225 Q 12.825 6.225 10.8 6.3 Q 8.775 6.375 7.125 6.525 Z"/>
    </g>
  </g>
</svg>
"""

FAVICON_DIR = Path("favicons/")
FAVICON_SPECS = [
    # Favicons
    #{"name": "favicon-16x16.png", "size": 16},
    #{"name": "favicon-32x32.png", "size": 32},
    {"name": "favicon-96x96.png", "size": 96},
    # Android icons
    {"name": "android-icon-36x36.png", "size": 36},
    {"name": "android-icon-48x48.png", "size": 48},
    {"name": "android-icon-72x72.png", "size": 72},
    {"name": "android-icon-96x96.png", "size": 96},
    {"name": "android-icon-144x144.png", "size": 144},
    {"name": "android-icon-192x192.png", "size": 192},
    # Apple icons
    {"name": "apple-icon-57x57.png", "size": 57},
    {"name": "apple-icon-60x60.png", "size": 60},
    {"name": "apple-icon-72x72.png", "size": 72},
    {"name": "apple-icon-76x76.png", "size": 76},
    {"name": "apple-icon-114x114.png", "size": 114},
    {"name": "apple-icon-120x120.png", "size": 120},
    {"name": "apple-icon-144x144.png", "size": 144},
    {"name": "apple-icon-152x152.png", "size": 152},
    {"name": "apple-icon-180x180.png", "size": 180},
    {"name": "apple-icon.png", "size": 180},
    {"name": "apple-icon-precomposed.png", "size": 180},
    # MS icons
    {"name": "ms-icon-70x70.png", "size": 70},
    {"name": "ms-icon-144x144.png", "size": 144},
    {"name": "ms-icon-150x150.png", "size": 150},
    {"name": "ms-icon-310x310.png", "size": 310},
]

# --- Configuration for logo.jpg ---
# The combined SVG content for the logo.jpg (RV inside a hexagon with specific colors)
LOGO_SVG_CONTENT_JPG = r"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <title>Logo</title>
  <g transform="translate(10, 5)">
    <!-- Hexagon Background -->
    <polygon
      id="Shape"
      stroke="#0A1128"
      stroke-width="4"
      fill="#0A1128"
      stroke-linecap="round"
      stroke-linejoin="round"
      points="40 0, 80 22.5, 80 67.5, 40 90, 0 67.5, 0 22.5"
    />
    
    <!-- RV Logo -->
    <g transform="translate(12, 26) scale(0.7)">
      <path d="M 65.7 53.325 L 57.675 53.325 L 38.4 2.7 L 45.375 0 L 61.875 45.525 L 78.45 0.225 L 84.9 2.7 L 65.7 53.325 Z M 37.275 51.075 L 30.6 54.225 L 24.075 39.975 Q 21.6 34.65 17.85 32.4 A 17.9 17.9 0 0 0 8.973 30.159 A 29.414 29.414 0 0 0 8.25 30.15 L 7.125 30.15 L 7.125 53.325 L 0 53.325 L 0 0.975 Q 3.975 0.6 7.612 0.412 Q 11.25 0.225 15.375 0.225 A 30.934 30.934 0 0 1 24.668 1.459 A 15.622 15.622 0 0 1 29.812 4.125 Q 34.65 8.025 34.65 14.175 Q 34.65 19.65 31.387 22.987 A 19.111 19.111 0 0 1 23.286 27.594 A 32.096 32.096 0 0 1 21.975 27.975 Q 24 28.875 25.575 30.112 Q 27.15 31.35 28.612 33.412 Q 30.075 35.475 31.575 38.775 L 37.275 51.075 Z M 7.125 6.525 L 7.125 24.15 L 15.375 24.15 Q 20.775 24.15 24.15 21.75 Q 27.525 19.35 27.525 14.85 Q 27.525 11.1 24.375 8.662 A 13.099 13.099 0 0 0 17.137 6.285 A 25.193 25.193 0 0 0 15.375 6.225 Q 12.825 6.225 10.8 6.3 Q 8.775 6.375 7.125 6.525 Z"
        fill="#FF8C00"
      />
    </g>
  </g>
</svg>
"""

def generate_favicon_pngs():
    """Generates PNG favicon files from the RV_SVG_CONTENT_FAVICON."""
    if not FAVICON_DIR.exists():
        FAVICON_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Generating favicon PNGs in {FAVICON_DIR}...")

    for spec in FAVICON_SPECS:
        output_path = FAVICON_DIR / spec["name"]
        try:
            svg2png(
                bytestring=RV_SVG_CONTENT_FAVICON.encode('utf-8'),
                write_to=str(output_path),
                output_width=spec["size"],
                output_height=spec["size"],
            )
            print(f"Generated: {output_path}")
        except Exception as e:
            print(f"Error generating {output_path}: {e}")
    print("PNG favicon generation complete.")

def generate_logo_jpg():
    """Generates logo.jpg from the LOGO_SVG_CONTENT_JPG."""
    output_dir = Path(".")
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    output_path_jpg = output_dir / "logo.jpg"

    print(f"Generating {output_path_jpg}...")

    try:
        # Convert SVG to PNG in memory
        png_data = svg2png(
            bytestring=LOGO_SVG_CONTENT_JPG.encode('utf-8'),
            output_width=100,
            output_height=100
        )

        # Open the PNG data with Pillow and save as JPG
        image = Image.open(io.BytesIO(png_data))
        if image.mode in ('RGBA', 'LA') or (image.mode == 'P' and 'transparency' in image.info):
            image = image.convert('RGB')
        image.save(output_path_jpg, "JPEG")
        print(f"Generated: {output_path_jpg}")

    except Exception as e:
        print(f"Error generating {output_path_jpg}: {e}")
    
    print("logo.jpg generation complete.")

if __name__ == "__main__":
    generate_favicon_pngs()
    generate_logo_jpg()
    print("All specified assets generated.")
    print("Remember to manually generate 'favicon.ico' using an online tool (like favicon.io) and place it in 'src/images/favicons/'.")