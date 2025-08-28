


num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))
divide = "cannot divide by 0" if num2 == 0 else f"Dividing one from another gives: {num1 / num2}"
floordivide = "cannot divide by 0" if num2 == 0 else f"using // gives: {num1 // num2}"
modulus = "cannot do modulus with num2 being 0" if num2 == 0 else f"getting the modulus from two numbers gives: {num1 % num2}"

message = f"""
Adding both gives: {num1 + num2}
Subtracting one from the other gives: {num1 - num2}
Multiplying both gives: {num1 * num2}
{divide}
{floordivide}
{modulus}
Powering one number by the other gives: {num1 ** num2}
"""
print(message)


