

name = input("What is your name? ")
age = int(input("What is your age? "))
answer = input("Do you like Python? ").lower()

if answer in ["yes", "yeah", "ye", "duh"]:
    answer = "love"
else:
    if answer in ["nah", "no", "fuck off"]:
        answer = "hate"

print(f"Hello, {name}! You are {age} and {answer} Python!")
