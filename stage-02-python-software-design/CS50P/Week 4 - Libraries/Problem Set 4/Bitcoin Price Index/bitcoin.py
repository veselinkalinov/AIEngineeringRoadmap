import sys

import requests

API_KEY = "YOUR_API_KEY"


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(
            f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}"
        )
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Request failed")

    data = response.json()
    price = float(data["data"]["priceUsd"])
    cost = bitcoins * price

    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()
