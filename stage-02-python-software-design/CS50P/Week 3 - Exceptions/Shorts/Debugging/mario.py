# Debugging the code using Run and Debug feature in Python

def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n: int) -> str:
    for i in range(n):
        # print(i, end=" ")
        print("#" * (i + 1))


if __name__ == "__main__":
    main()
