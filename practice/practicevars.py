

age = int(input("What is your age? "))
studentid = input("Do you have a student ID? Y/N ").upper()
tickets = int(input("how many tickets do you want? "))

adultprice = 12
teenprice = 10
discount = .2
baseprice =  adultprice if age >=18 else teenprice
total = baseprice * tickets
subtotal = total * discount

if age <= 12:
    print("Sorry, you're too young for this movie")
elif age in [13, 14, 15, 16, 17]:
    if studentid == "Y":
        print("You get a student discount!")
        print(f"Total cost = ${subtotal:.2f}")
    else:
        print("Regular teen ticket price applies")
        print(f"Total cost = ${total:.2f}")
elif age >= 18:
    if studentid == "Y":
        print("You get a student discount on the adult ticket!")
        print(f"Total cost = ${subtotal:.2f}")
    else:
        print("Full adult ticket price applies")
        print(f"Total cost = ${total:.2f}")



