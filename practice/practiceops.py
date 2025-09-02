age = int(input("How old are you? "))
id = input("Do you have an ID? Y/N ").upper()
vip = input("Are you a VIP memeber? Y/N ").upper()

if vip == "Y": print("GET IN HERE!")

elif age >= 21 and id == "Y": print("You may enter!")

elif age <21 or id == "N": print("GET OUT OF HERE!")

#second optoin is
import sys

vip = input("Are you a VIP memeber? Y/N ").upper()
if vip == "Y":
    print("GET IN HERE!")
    sys.exit

age = int(input("How old are you? "))
if age == "N":
    print("GET OUT OF HERE!")
    sys.exit

id = input("Do you have an ID? Y/N ").upper()
if id == "N":
    print("GET OUT OF HERE!")
    sys.exit


fruits = {"apple": 2, "banana": 5}

# Key exists
print(fruits.get("apple"))       # Output: 2

# Key does not exist, no default
print(fruits.get("orange"))      # Output: None

# Key does not exist, with default
print(fruits.get("orange", 0))   # Output: 0

