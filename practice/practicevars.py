num1 = int(input("First Number? "))
num2 = int(input("Second Number? "))
operation = input("Choose an Operation (+, -, /, *, //, %, **)")

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    if num2 == 0:
        result = "Cannot divide by zero"
    else:
        result = num1 / num2

elif operation == "//":
    if num2 == 0:
        result = "Cannot // by zero"
    else:
        result = num1 // num2

elif operation == "%":
    if num2 == 0:
        result = "Cannot modulus by zero"
    result = num1 % num2

elif operation == "**":
    result = num1 ** num2

else:
    print("can't do that")

print(f"You chose {num1} {operation} {num2} = {result}")

