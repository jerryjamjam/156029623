

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
    operation = num1 / num2

elif operation == "//":
    operation = num1 // num2

elif operation == "%":
    operation = num1 % num2

elif operation == "**":
    operation = num1 ** num2

else:
    print("can't do that")


print(f"You chose {num1} {operation} {num2}")
