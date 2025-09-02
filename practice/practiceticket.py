age = int(input("What is your age? "))
studentid = input("Do you have a student ID? Y/N ").upper()
tickets = int(input("how many tickets do you want? "))

adultprice = 12
teenprice = 10
discount = .2
adult_discount = (tickets * adultprice) - (discount * (adultprice * tickets))
teen_discount = (tickets * teenprice) - (discount * (teenprice * tickets))

if age <= 12:
    print("Sorry, you're too young for this movie")
elif 13 <= age <= 17:
    if studentid == "Y":
        print("You get a student discount!")
        print(f"Total cost = ${teen_discount:.2f}")
    else:
        print("Regular teen ticket price applies")
        print(f"Total cost = ${tickets * teenprice:.2f}")
elif age >= 18:
    if studentid == "Y":
        print("You get a student discount on the adult ticket!")
        print(f"Total cost = ${adult_discount:.2f}")
else:
    print("Full adult ticket price applies")
    print(f"Total cost = ${tickets * adultprice:.2f}")
