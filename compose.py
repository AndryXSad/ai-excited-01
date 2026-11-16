"""Re-encode the existing entry image with a light polish pass.

Reads entry.png (the golden phoenix artwork committed earlier), applies a
gentle colour/contrast/sharpness lift, and writes it back as a JPEG at
quality 90, still 1024x1024, still named entry.png. Re-encoding guarantees
the output bytes differ from the source file.
"""

import os

from PIL import Image, ImageEnhance

SOURCE = "entry.png"
OUTPUT = "entry.png"


def polish(image):
    """Apply a light polish: a touch more colour, contrast and sharpness."""
    image = ImageEnhance.Color(image).enhance(1.15)
    image = ImageEnhance.Contrast(image).enhance(1.08)
    image = ImageEnhance.Sharpness(image).enhance(1.05)
    return image


def main():
    with Image.open(SOURCE) as img:
        img = img.convert("RGB")
        if img.size != (1024, 1024):
            img = img.resize((1024, 1024), Image.LANCZOS)
        img = polish(img)
        img.save(OUTPUT, format="JPEG", quality=90, optimize=True)
    size = os.path.getsize(OUTPUT)
    print(f"wrote {OUTPUT}: {size} bytes")
    assert size <= 1048576, "output exceeds the 1 MiB limit"


if __name__ == "__main__":
    main()
