import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    if not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    try:
        data = []
        with open(sys.argv[1]) as table:
            reader = csv.reader(table)
            headers = next(reader)
            for row in reader:
                data.append(row)
            print(tabulate(data, headers, tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()



