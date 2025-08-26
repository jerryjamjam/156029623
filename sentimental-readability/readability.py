string = input("What is your input? ")

charcount = 0
for i in range(len(string)):
    if string[i].isalpha():
        charcount = charcount + 1

wordcount = len(str.split(string))

sentencecount = string.count('.') + string.count('!') + string.count('?')

l = charcount / wordcount * 100
s = sentencecount / wordcount * 100
index = round(.0588 * l - 0.296 * s - 15.8)
if index < 1:
    print("Before Grade 1")
if index > 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
