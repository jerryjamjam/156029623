import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():
    number = input("Number: ")
    if match := re.search(r"(\+\d{1,3}) \d{3}-?\d{3}-?\d{4}", number):
        country_code = match.group(1)
        print(locations[country_code])
    else:
        print("invalid")

main()
 