import re
import sys

def main():
    try:
        hrs = input("Hours? ").upper()
        extracted_tuple = extract(hrs)
        if extracted_tuple is None:
            raise ValueError

        time1, time2, part1, part2, addon1, addon2, connect1, connect2 = extracted_tuple
        converted_times = convert(time1, time2, part1, part2)
        if converted_times is None:
            raise ValueError

        concat = concatinate(*converted_times, addon1, addon2, connect1, connect2)
        if concat is None:
            raise ValueError

        print(concat)
    except ValueError:
        print("ValueError")
        sys.exit(1)

def extract(hrs):
    if extracted_time := re.search(r"(\d{1,2})(:)?(\d{2})?\s(AM|PM)\s+to\s+(\d{1,2})(:)?(\d{2})?\s(AM|PM)", hrs, re.IGNORECASE):
        time1 = extracted_time.group(1)
        time2 = extracted_time.group(5)
        part1 = extracted_time.group(4)
        part2 = extracted_time.group(8)
        connect1 = extracted_time.group(2)
        connect2 = extracted_time.group(6)
        if connect1 == None:
            connect1 = ":"
        if connect2 == None:
            connect2 = ":"
        if extracted_time.group(3) == None:
            addon1 = "00"
        else:
            addon1 = extracted_time.group(3)
        if extracted_time.group(7) == None:
            addon2 = "00"
        else:
            addon2 = extracted_time.group(7)
        if int(time1) >= 13 or int(time2) >= 13:
            print("ValueError")
            sys.exit(1)

        if int(addon1) >= 60 or int(addon2) >= 60:
            print("ValueError")
            sys.exit(1)

        return time1, time2, part1, part2, addon1, addon2, connect1, connect2
    else:
        return None

def convert(time1, time2, part1, part2):
    converted_time1 = "00" if part1 == "AM" and time1 == "12" else time1 if part1 == "PM" and time1 == "12" else str(int(time1) +12) if part1 == "PM" else time1
    converted_time2 = "00" if part2 == "AM" and time2 == "12" else time2 if part2 == "PM" and time1 == "12" else str(int(time2) +12) if part2 == "PM" else time2
    if len(converted_time1) == 1:
        converted_time1 = "0" + converted_time1
    if len(converted_time2) == 1:
        converted_time2 = "0" + converted_time2
    return converted_time1, converted_time2

def concatinate(converted_time1, converted_time2, addon1, addon2, connect1, connect2):
    concat = f"{converted_time1}{connect1}{addon1} to {converted_time2}{connect2}{addon2}"
    return concat

if __name__ == "__main__":
    main()


