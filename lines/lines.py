import sys

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    if not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

    try:
        with open(sys.argv[1]) as file:
            rows = 0
            tripple = False
            for row in file:
                if row.lstrip().startswith('"""') or row.lstrip().startswith('"""'):
                    if row.lstrip().startswith("'''") or row.lstrip().startswith("'''"):
                        tripple = not tripple
                if row.lstrip() and not row.lstrip().startswith("#") and not tripple:
                    rows += 1
            print(rows, end="")
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
if __name__ == "__main__":
    main()
