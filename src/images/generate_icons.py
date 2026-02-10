from PIL import Image
from pathlib import Path

SRC = Path("logo.png")
OUT = Path("favicons")

OUT.mkdir(exist_ok=True)

# Load source image
img = Image.open(SRC).convert("RGBA")

def save_icon(size: int, name: str):
    resized = img.resize((size, size), Image.LANCZOS)
    resized.save(OUT / name, format="PNG")

# Android legacy icons
for s in [36, 48, 72, 96, 144, 192]:
    save_icon(s, f"android-icon-{s}x{s}.png")

# Android Chrome / PWA
save_icon(192, "android-chrome-192x192.png")
save_icon(512, "android-chrome-512x512.png")

# Apple icons
for s in [57, 60, 72, 76, 114, 120, 144, 152, 180]:
    save_icon(s, f"apple-icon-{s}x{s}.png")

# Apple special icons
save_icon(180, "apple-touch-icon.png")
save_icon(180, "apple-icon-precomposed.png")
save_icon(180, "apple-icon.png")

# Favicons
save_icon(16, "favicon-16x16.png")
save_icon(32, "favicon-32x32.png")
save_icon(96, "favicon-96x96.png")

# favicon.ico (multi-size)
img.save(
    OUT / "favicon.ico",
    format="ICO",
    sizes=[(16, 16), (32, 32)]
)

# Microsoft tiles
for s in [70, 144, 150, 310]:
    save_icon(s, f"ms-icon-{s}x{s}.png")

print("✅ All favicons generated in ./favicons")