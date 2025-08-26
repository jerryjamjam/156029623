import re

def main():
    print(parse(input("HTML: ")))

def parse(html):
    url_match = re.search(r'src="([^"]+)"', html)
    if url_match:
        url = url_match.group(1)
        if pattern := re.search(r"(http)s?(://)(?:www\.)?(youtu)(be)\.com(/)embed/(.+)", url):
            sharable = pattern.group(1) + "s" + pattern.group(2) + pattern.group(3) + "." + pattern.group(4) + pattern.group(5) + pattern.group(6)
            return f"{sharable}"

if __name__ == "__main__":
    main()


