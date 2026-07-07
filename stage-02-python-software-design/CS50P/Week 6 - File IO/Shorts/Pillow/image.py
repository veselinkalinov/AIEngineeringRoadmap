# pyrefly: ignore [missing-import]
from PIL import Image, ImageFilter


def main():
    with Image.open(
        "C:\Projects\Road to AI Engineer\stage-02-python-software-design\CS50P\Week 6 - File IO\Shorts\Pillow\in.jpeg"
    ) as img:
        print(img.size)
        print(img.format)

        image_blur = img.filter(ImageFilter.BLUR)
        image_blur.save(
            "C:\Projects\Road to AI Engineer\stage-02-python-software-design\CS50P\Week 6 - File IO\Shorts\Pillow\image_blur.jpeg"
        )

        image_edges = img.filter(ImageFilter.FIND_EDGES)
        image_edges.save(
            "C:\Projects\Road to AI Engineer\stage-02-python-software-design\CS50P\Week 6 - File IO\Shorts\Pillow\image_edges.jpeg"
        )

        image_rotate = img.rotate(180)
        image_rotate.save(
            "C:\Projects\Road to AI Engineer\stage-02-python-software-design\CS50P\Week 6 - File IO\Shorts\Pillow\image_rotate.jpeg"
        )


if __name__ == "__main__":
    main()
