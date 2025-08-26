def main():
    word = input("What do you have to say? ")
    result = shorten(word)
    print(result)

def shorten(word):
    vowels = "aeioyAEIOY"
    joined = "".join(char for char in word if char not in vowels)
    return joined

if __name__ == "__main__":
    main()
