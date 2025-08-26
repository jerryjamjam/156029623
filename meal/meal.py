def main():
    time = input("what time is it? ")
    time = convert(time)
    try:
        if time >= 7 and time <= 8:
            print("breakfast time")

        elif time >= 12 and time <= 13:
            print("lunch time")

        elif time >= 18 and time <= 19:
            print("dinner time")
    except(TypeError):
            print("Please enter valid time")

def convert(time):
    try:
        hours, minutes = map(int, time.split(":"))
        time = hours + minutes / 60
        return time
    except(ValueError):
        return None

if __name__ == "__main__":
    main()
