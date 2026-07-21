# pyrefly: ignore [missing-import]
from pathlib import Path

from PIL import Image, ImageFilter


def main():
    # Legacy input/output paths used C:\Projects\Road to AI Engineer\...\Pillow\.
    image_dir = Path(__file__).parent

    with Image.open(image_dir / "in.jpeg") as img:
        print(img.size)
        print(img.format)

        image_blur = img.filter(ImageFilter.BLUR)
        image_blur.save(image_dir / "image_blur.jpeg")

        image_edges = img.filter(ImageFilter.FIND_EDGES)
        image_edges.save(image_dir / "image_edges.jpeg")

        image_rotate = img.rotate(180)
        image_rotate.save(image_dir / "image_rotate.jpeg")


if __name__ == "__main__":
    main()
