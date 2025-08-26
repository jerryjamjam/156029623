import sys
from fractions import Fraction

def main():
    while True:
        try:
            userinput = input("Fraction: ")
            percent = convert(userinput)
            result = gauge(percent)
            print(result)
            sys.exit(1)
        except ValueError:
            print("Please input a fraction")
        except ZeroDivisionError:
            print("Please input a fraction")
        except TypeError:
            print("Please input a fraction")

def convert(fraction):
    try:
        num, denom = fraction.split('/')
        num = int(num)
        denom = int(denom)
        if num > denom:
            raise ValueError
        if num < 0 or denom < 0:
            raise ValueError("Negative numbers are not allowed.")
        fract = Fraction(fraction)
        fract = round(float(fract) * 100)
        return(fract)
    except ValueError:
        print("Please input a fractionC1")
        raise ValueError
    except ZeroDivisionError:
        print("Please input a fractionC2")
        raise ZeroDivisionError


def gauge(percentage):
    if percentage >= 99:
        return("F")
    elif percentage <= 1:
        return("E")
    else:
        return(f"{percentage}%")

if __name__ == "__main__":
    main()
