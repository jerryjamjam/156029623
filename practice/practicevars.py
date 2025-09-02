

num1 = int(input("First Number? "))
num1 = int(input("Second Number? "))
operation = input("Choose an Operation (+, -, /, *, //, %, **)")

if operation == "+":
    plus = num1 + num2

elif operation == "-":
    minus = num1 + num2

elif operation == "*":
    times = num1 + num2

elif operation == "/":
    divide = num1 + num2
    

elif operation == "//":
    floordivide = num1 + num2

elif operation == "%":
    modulus = num1 + num2

elif operation == "**":
    kwargs = num1 + num2

else:
    print("can't do that")

