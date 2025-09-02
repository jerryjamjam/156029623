num1 = int(input("First Number? "))
num2 = int(input("Second Number? "))
operation = input("Choose an Operation (+, -, /, //, %, *, **) ")

operations = {
    "+": add
    "-": sub
    "/": divide
    "//": floordivide
    "%": modulus
    "*": times
    "**": expo
}

def add(num1, num2):
    num1 + num2

def sub(num1, num2):
    num1 - num2

def divide(num1, num2):
    num1 / num2


result = operations[{operation}](num1, num2)

if operation == "+":
    result = num1 + num2
    print(f"You chose {num1} {operation} {num2} -> Error: {result}")
else:
    print(f"You chose {num1} {operation} {num2} -> Result: {result}")

