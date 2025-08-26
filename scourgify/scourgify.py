import csv
import sys

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    if not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    try:
        with open(sys.argv[1]) as file:
           reader = csv.DictReader(file)
           new_rows = [{"first": row["name"].split(", ")[1], "last": row["name"].split(", ")[0], "house": row["house"].split(", ")} for row in reader]
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

    with open(sys.argv[2], 'w', newline= '') as newfile:
        writer = csv.DictWriter(newfile, fieldnames = ["first", "last", "house"])
        writer.writeheader()
        writer.writerow(new_rows)

if __name__ == "__main__":
    main()


