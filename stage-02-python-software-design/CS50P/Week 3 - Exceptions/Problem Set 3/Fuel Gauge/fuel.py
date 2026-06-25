def main():
    while True:
        try:
            frac = input("Fraction: ")
            x, y = convert(frac)

            if y == 0:
                continue

            if x < 0 or y < 0:
                continue

            if x > y:
                continue

            fuel = (x/y)*100
            if fuel <= 1:
                print("E")
            elif fuel >= 99:
                print("F")
            else:
                print(f"{fuel:.0f}%")
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction: str) -> int:
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    return x, y


if __name__ == "__main__":
    main()
