num1 = int(input("First Number? "))
num2 = int(input("Second Number? "))
operation = input("Choose an Operation (+, -, /, *, //, %, **)")

if operation == "+":
    operation = num1 + num2

elif operation == "-":
    operation = num1 - num2

elif operation == "*":
    operation = num1 * num2

elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        operation = num1 / num2

elif operation == "//":
    if num2 == 0:
        print("Cannot // by zero")
    else:
        operation = num1 // num2

elif operation == "%":
    if num2 == 0:
        print("Cannot modulus by zero")
    operation = num1 % num2

elif operation == "**":
    operation = num1 ** num2

else:
    print("can't do that")

if num2 == 0:
    print(f"You chose {num1} {operation} {num2} ")
else:
    print(f"You chose {num1} {operation} {num2}NO")
