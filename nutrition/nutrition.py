import sys
#i could have made the og dict with all lowercase, but wanted to make it a little more challenging.
#simply needed to make a copy of the dict with .lower() included and use the og value in the new dict.
def main():
    fruits =   {
        "Apple": "130",
        "Avocado": "50",
        "Banana": "110",
        "Cantaloupe": "50",
        "Grapefruit": "60",
        "Grapes": "90",
        "Honeydew Melon": "50",
        "Kiwifruit": "90",
        "Lemon": "15",
        "Lime": "20",
        "Nectarine": "60",
        "Orange": "80",
        "Peach": "60",
        "Pear": "100",
        "Pinapple": "50",
        "Plums": "70",
        "Strawberries": "50",
        "Sweet Cherries": "100",
        "Tangerine": "50",
        "Watermelon": "80"
    }
    new_dict = {}
    for fruit in fruits:
         new_dict[fruit.lower()] = fruits[fruit]

    fruit = input("Item: ").lower()
    if fruit in new_dict:
            calories = new_dict[fruit]
            print(f"{calories}")
    else:
        sys.exit()

main()


