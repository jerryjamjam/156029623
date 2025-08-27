


num1 = int(input("What number are you thinking of? "))
num2 = int(input("What number are you thinking of? "))

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
Powering one number by the other gives: {exponential}
"""
print(message)

