def main():
    while True:
        au = input("AU: ")
        try:
            au = float(au)
            break
        except ValueError:
            continue
    print(f"{au} AU is {convert(au)} m")


def convert(au: float) -> float:
    if not isinstance(au, (int, float)):
        raise TypeError("au must be an int or a float")
    return au * 149597870700
