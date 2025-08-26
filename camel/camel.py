from re import split

def main():
    words = input("What is your input? ")
    parts = split("(?<=[a-z])(?=[A-Z])", words)
    parts = [part.lower() for part in parts]
    joined = "_".join(parts)
    print(joined)

main()
