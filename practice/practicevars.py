num1 = int(input("First Number? "))
num2 = int(input("Second Number? "))
operation = input("Choose an Operation (+, -, /, //, %, *, **) ")


def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def times(num1, num2):
    return num1 * num2

def expo(num1, num2):
    return num1 ** num2

def divide(num1, num2):
    if num2 == 0:
        return None
    else:
        return num1 / num2

def floordivide(num1, num2):
    if num2 == 0:
        return None
    else:
        return num1 // num2

def modulus(num1, num2):
    if num2 == 0:
        return None
    else:
        return num1 % num2

operations = {
    "+": add,
    "-": sub,
    "/": divide,
    "//": floordivide,
    "%": modulus,
    "*": times,
    "**": expo
}

result = operations[operation](num1, num2)

if result == None:
    if operation is "/":
        print(f"You chose {num1} {operation} {num2} -> Error: Cannot divide by zero")
    elif operation is "//":
        print(f"You chose {num1} {operation} {num2} -> Error: Cannot floordivide by zero")
    else:
        print(f"You chose {num1} {operation} {num2} -> Error: Cannot modulus by zero")
else:
    print(f"You chose {num1} {operation} {num2} -> Result: {result}")

