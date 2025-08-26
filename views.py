import csv
import numpy as np
from PIL import Image

def main():
    yesorno = input("do you want to write? ")
    if yesorno == "yes":
        dictwriter()
    elif yesorno == "no":
        dictreader()

def dictwriter():
    number = input("Number? ")
    name = input("Name? ")
    othername = input("Othername? ")

    with open("view.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames = ["number", "name", "othername"])
        writer.writerow({"number": number, "name": name, "othername": othername})

def dictreader():
    with open("view.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            brightness = calculate_brightness(f"{row["number"]}.jpeg")
            print(row["name"], brightness)


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness

if __name__ == "__main__":
    main()
