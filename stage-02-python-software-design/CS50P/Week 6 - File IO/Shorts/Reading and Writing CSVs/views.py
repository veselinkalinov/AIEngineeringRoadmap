import csv
from pathlib import Path

import numpy as np
from PIL import Image


def main():
    csv_path = Path(__file__).with_name("views.csv")
    csv_write = Path(__file__).with_name("analysis.csv")
    with (
        csv_path.open("r", newline="") as views,
        csv_write.open("w", newline="") as analysis,
    ):
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            row["brightness"] = round(
                calculate_brightness(Path(__file__).with_name(f"{row['id']}.jpeg")), 2
            )
            writer.writerow(row)


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


if __name__ == "__main__":
    main()
