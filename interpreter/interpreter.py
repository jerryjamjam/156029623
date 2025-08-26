def main():
    try:
        components = input("What is your operation? ").split()
        x = float(components[0])
        y = components[1]
        z = float(components[2])

        if y == "-":
            print("{:.1f}".format(x - z))
        elif y == "+":
            print("{:.1f}".format(x + z))
        elif y == "/":
            print("{:.1f}".format(x / z))
        elif y == "*":
            print("{:.1f}".format(x * z))
        else:
            print("please choose valid operator")

    except (ValueError, IndexError):
        print("Invalid input")

main()

