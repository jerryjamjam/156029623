def main():
    answer = input("What is the Great Question of Life, the Universe and Everything? ").lower().strip()
    legit_answers = ["42", "forty two", "forty-two"]
    if answer in legit_answers:
        print("Yes")
    else:
        print("No")

main()
