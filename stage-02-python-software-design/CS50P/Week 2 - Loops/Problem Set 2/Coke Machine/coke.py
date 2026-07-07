def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        coin = int(input("Insert coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            amount_due -= coin
    print(f"Change owed: {abs(amount_due)}")


if __name__ == "__main__":
    main()
