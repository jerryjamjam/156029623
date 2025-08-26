import csv
import numpy as np
from PIL import Image

def main():
    yesorno = input("do you want to write? ")
    if yesorno == "yes":
        dictwriter()
    elif yesorno == "no":
        dictreader()
    else:
        print("YES OR NO!!!")

def dictwriter():
    number = input("Number? ")
    name = input("Name? ")
    othername = input("Othername? ")

    filename = f"{number}.jpg"
    brightness = calculate_brightness(filename)

    with open("view.csv", "a", newline='') as analysis:
        writer = csv.DictWriter(analysis, fieldnames = ["number", "name", "othername", "brightness"])
        if analysis.tell() == 0: #returns the current byte position in the file, AKA THE POINTER
            writer.writeheader()
        writer.writerow({"number": number, "name": name, "othername": othername, "brightness": brightness})

def dictreader():
    with open("view.csv", "r") as view:
        reader = csv.DictReader(view)
        for row in reader:
            brightness = calculate_brightness(f"{row["number"]}.jpg")
            print(row["name"], round(brightness, 2))

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness

if __name__ == "__main__":
    main()
