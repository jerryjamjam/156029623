import random

def main():
    while True:
        try:
            inputseed = int(input("Level: "))
            if inputseed > 0:
                break
            else:
                print("f")
        except ValueError:
            print("f")

    random.seed(inputseed)
    random_num = random.randint(1, inputseed)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                print("f")
            elif guess == random_num:
                print("Just right!")
                break
            elif guess < random_num:
                print("Too small!")
            elif guess > random_num:
                print("Too large!")
        except ValueError:
            print("f")
main()

