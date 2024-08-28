import json
import requests
import sys

def main():
    # Make sure there is a command-line argument
    if len(sys.argv) != 2:
      sys.exit("Missing command-line argument")
    # Try to convert the argument into a float
    try:
        bitcoins = float(sys.argv[1])
        if bitcoins<0:
            raise ValueError
    except ValueError:
        sys.exit("Command-line argument is not a number")
    # Fetch the bitcoin price from Coindesk API

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        priceperbitcoin = data["bpi"]["USD"]["rate_float"]
        #data["bpi"]["USD"]["rate_float"]: This line navigates through the nested dictionary to extract the price of Bitcoin in USD.
    except requests.RequestException:
        sys.exit()
    # Calculate the cost of the specified number of Bitcoins
    cost = bitcoins*priceperbitcoin

    # Print the cost formatted to four decimal places with a thousands separator
    print(f"${cost:,.4f}")

if __name__ == "__main__":
    main()
