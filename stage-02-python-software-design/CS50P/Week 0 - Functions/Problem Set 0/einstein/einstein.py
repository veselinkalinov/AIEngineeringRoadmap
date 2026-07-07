def energy_formula(mass: int) -> int:
    energy = mass * pow(3 * (10 ** 8), 2)
    return energy


def main():
    mass = int(input("m: "))
    energy = energy_formula(mass)
    print(f"E: {energy}")


if __name__ == "__main__":
    main()
