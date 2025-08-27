


num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))


message = f"""
Adding both gives: {num1 + num2}
Subtracting one from the other gives: {num1 - num2}
Multiplying both gives: {num1 * num2}
Dividing one from another gives: {num1 / num2}
Using // gives: {num1 // num2}
Getting the modulus from two numbers gives: {num1 & num2}
Powering one number by the other gives: {num1 ** num2}
"""
print(message)


