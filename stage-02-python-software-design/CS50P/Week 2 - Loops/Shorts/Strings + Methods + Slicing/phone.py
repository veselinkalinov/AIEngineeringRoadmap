def main():
    phone = "617-495-1000"
    print(phone[:3], end="\n")  # Inclusive - 0/blank idx, Exclusive - 3 idx
    print(phone[-4:])


if "__main__" == __name__:
    main()
