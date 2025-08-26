def main():
    while True:
        months = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }
        try:
            date = input("Date: ").strip()

            if "/" in date:
                parts = date.split("/")
                if parts[0].isdigit():
                    month, day, year = int(parts[0]), parts[1], parts[2]
                    if int(parts[1]) <= 31:
                        if 1 <= int(month) <= 12:
                            print(f"{int(year)}-{int(month):02}-{int(day):02}")
                            break

            elif " " in date and "," in date:
                parts = date.split(" ")
                if parts[0].isdigit():
                    continue
                month, day, year = parts[0], int(parts[1].strip(",")), int(parts[2])
                if day <= 31:
                        if month in months:
                            print(f"{int(year)}-{months[month]:02}-{day:02}")
                            break
            if "," not in date or "/" not in date:
                continue

        except ValueError:
            break
main()
