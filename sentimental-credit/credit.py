import re

while True:
    cardnumber = input("Card Number: ")
    cardnumber = re.sub("-", "", cardnumber)
    if len(cardnumber) in [13, 15, 16]:
        number_convert = str(cardnumber)
        reversed_num = cardnumber[::-1]
    sum = 0
    for i in range(1, len(cardnumber), 2):
        digit = int(cardnumber[i])
        digit = digit * 2
        if digit > 9:
            digit = digit - 9
        sum = sum + digit
    sum2 = 0
    for j in range(0, len(cardnumber), 2):
        digit2 = int(cardnumber[j])
        sum2 = sum2 + digit2
    sum = sum + sum2
    print(sum)
    if sum % 10 != 0:
            print("INVALID")
    first2 = int(cardnumber[:2])
    if first2 == 34 or first2 == 37:
        print("AMEX")
    if first2 >= 51 and first2 <= 55:
        print("MASTERCARD")
    if int(cardnumber[0]) == 4:
        print("VISA")
    else:
        print("INVALID")
    break

