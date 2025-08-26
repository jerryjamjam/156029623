def main():
    x = get_int()
    print(f"{x}")

def get_int():
    while True:
        try:
            x = int(input("What x!? "))
        except ValueError:
            print("are you f***** DUMB!?")
        else:
            return x
main()
