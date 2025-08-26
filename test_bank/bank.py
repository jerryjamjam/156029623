import sys

def main():
    greeting = input("how will you greet the human? ").strip()
    print(value(greeting.lower()))

def value(greeting):
    if "hello" in greeting:
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
