import inflect

def main():
    inf_class = inflect.engine()
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            if name.isalnum():
                names.append(name)
        except EOFError:
            break
        output = inf_class.join(names)
    print(f"\nAdieu, adieu, to {output}")

main()
