import requests
import sys

def main():
#get argv then change the argv to a float
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    amount = sys.argv[1]
    try:
        purchase = float(amount)
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

# Queries the API for the CoinDesk Bitcoin Price Index
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    usd_price = float(data["bpi"]["USD"]["rate"].replace(",", ""))
    usd_price = usd_price * purchase
    print(f"${usd_price:,.4f}")

main()
# we use float for purchase and for the data response because we want to make sure we can
# safely multiply the two

