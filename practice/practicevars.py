

name = input("What is your name? ")
age = int(input("What is your age? "))
answer = input("Do you like Python? ").lower()

if answer in ["yes", "yeah", "ye", "duh"]:
    answer = "love"
elif answer in ["nah", "no", "fuck off"]:
    answer = "hate"
else:
    answer = "i don't know"


print(f"Hello, {name}! You are {age} and {answer} Python!")
