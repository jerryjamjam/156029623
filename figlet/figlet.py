from sys import argv
import sys
import pyfiglet
import random

def main():
        figlet = pyfiglet.Figlet()
        if len(argv) == 2:
                sys.exit(1)
        if argv[1] != "-f" and argv[1] != "--font":
            sys.exit(1)
        elif len(argv) == 1:
            user_input = input("Input: ")
            font_list = figlet.getFonts()
            random_font = random.choice(font_list)
            figlet = pyfiglet.Figlet(font = random_font)
            output = figlet.renderText(user_input)
            print(f"Output:\n{output}")

        elif len(argv) == 3 and (argv[1] == "-f" or argv[1] == "--font"):
            font_name = argv[2]
            figlet = pyfiglet.Figlet(font = font_name)
            user_input = input("Input: ")
            output = figlet.renderText(user_input)
            print(f"Output:\n\n{output}")

main()



