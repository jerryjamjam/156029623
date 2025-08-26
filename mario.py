def main():
    size = int(input("square size HUH!? "))
    print_square(size)

def print_square(size):
    for _ in range(size):
        print("#" * size)

main()
