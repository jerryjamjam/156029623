import datetime
import inflect
import sys

def main():
    birth_date, today = get_dates()
    mins_lived = birth_date_conversion(birth_date, today)
    words = word_conversion(mins_lived)
    print(f"{words} minutes")

def get_dates():
        user_input1 = input("What is your birthday? ")
        try:
            birth_date = datetime.datetime.strptime(user_input1, "%Y-%m-%d")
            birth_date = birth_date.date()
            today = datetime.date.today()
            return birth_date, today
        except ValueError:
            print("please use YMD xxxx-xx-xx format")
            sys.exit(1)
            
def birth_date_conversion(birth_date, today):
    timedelta = today - birth_date
    seconds_lived = timedelta.total_seconds()
    mins_lived = seconds_lived / 60
    return mins_lived

def word_conversion(mins_lived):
    mins_lived = int(mins_lived)
    words = inflect.engine()
    words = words.number_to_words(mins_lived)
    new_words = words.replace(" and", "")
    return new_words.capitalize()

if __name__=="__main__":
    main()

