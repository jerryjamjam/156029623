num1 = int(input("First Number? "))
num2 = int(input("Second Number? "))
operation = input("Choose an Operation (+, -, /, *, //, %, **) ")

operations = {
    
}

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
    else:
        result = num1 % num2

elif operation == "**":
    result = num1 ** num2

else:
    print("can't do that")

if num2 == 0 and operation in [/, //, %]:
    print(f"You chose {num1} {operation} {num2} -> Error: {result}")
else:
    print(f"You chose {num1} {operation} {num2} -> Result: {result}")

