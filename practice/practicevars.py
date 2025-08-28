

age = int(input("What is your age? "))
studentid = input("Do you have a student ID? Y/N ").upper()



if age <= 13:
    print("Sorry, you're too young for this movie")
elif age in [13, 14, 15, 16, 17]:
    if studentid == "Y":
        print("You get a student discount")
    else:
        print("Regular teen ticket price applies")
elif age >= 18:
    if studentid == "Y":
        print("You get a student discount on the adult ticket!")
else:
    print("Full adult ticket price")


