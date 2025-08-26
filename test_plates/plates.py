import sys

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
        sys.exit(1)

def is_valid(plate):
    if not plate.isalnum():
        return False

    if len(plate) > 6 or len(plate) < 2:
        return False

    if not plate[0].isalpha() and not plate[1].isalpha():
        return False

    #index is a variable that holds the currect index of the loop and enumerate creates a tuple that stores the index and what it is.
    first_digit = None
    for index, char in enumerate(plate):
        if char.isdigit():
            first_digit = index
            break

    if first_digit is None:
        return True

    if plate[first_digit] == '0':
        return False

    if not plate[first_digit:].isdigit():
            return False

if __name__ == "__main__":
    main()



