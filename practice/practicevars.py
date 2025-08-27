


num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))

add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divide = num1 / num2
floordivide = num1 // num2
modulus = num1 % num2
exponential = num1 ** num2

message = f"""
Adding both gives: {add}
Subtracting one from the other gives: {subtract}
Multiplying both gives: {multiply}
Dividing one from another gives: {divide}
Using // gives: {floordivide}
Getting the modulus from two numbers gives: {modulus}
Powering one number by the other gives: {exponential}
"""
print(message)

