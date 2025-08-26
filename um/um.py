import re
import sys

def main():
    input_text = input("Text: ")
    number_of_ums = count(input_text)
    if number_of_ums is None:
        raise ValueError
    print(number_of_ums)

def count(input_text):
    matches = re.findall(r"\bum\b", input_text, re.IGNORECASE)
    number_of_ums = len(matches)
    return number_of_ums

if __name__ == "__main__":
    main()
