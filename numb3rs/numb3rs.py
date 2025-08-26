import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])$"
    return bool(re.match(pattern, ip))

if __name__ == "__main__":
    main()


