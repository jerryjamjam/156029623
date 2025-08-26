import sys
import string

def main():
        words = input("What do you have to say? ")
        for letter in words:
                if letter in string.punctuation or not letter.isalpha():
                    print(letter)
                    sys.exit(1)
        result = shorten(words)
        print(result)

def shorten(words):
    vowels = "aeiouAEIOU"
    joined = "".join(char for char in words if char not in vowels)
    return joined

if __name__ == "__main__":
    main()
