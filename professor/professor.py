import random


def main():
    level = get_level()
    pairs = generate_integer(level)
    score = 0
    for x, y in pairs:
        problem = f"{x} + {y} = "
        answer = x + y
        attemptcount = 0

        while attemptcount < 3:
            try:
                attempt = int(input(f"{problem} "))
                if attempt == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attemptcount += 1
            except ValueError:
                print("please enter an integer")
        if attemptcount == 3:
            print(f"{problem} {answer}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                return level
        except ValueError:
            continue
def generate_integer(level):
    pairs = []
    while len(pairs) < 10:
        if level == 1:
            randint1 = random.randint(0, 9)
            randint2 = random.randint(0, 9)
        elif level == 2:
            randint1 = random.randint(10, 99)
            randint2 = random.randint(10, 99)
        elif level == 3:
            randint1 = random.randint(100, 999)
            randint2 = random.randint(100, 999)
        pairs.append((randint1, randint2))
    return pairs


if __name__ == "__main__":
    main()
