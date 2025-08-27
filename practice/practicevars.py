

name = "Jared"

age = 32

answer = input("Do you like Python? ").lower()
if answer in ["yes", "yeah", "ye", "duh"]:
    answer = "love"
elif answer in ["nah", "no", "fuck off"]:
    answer = "hate"

print(f"Hello, {name}! You are {age} and {answer} Python!")
