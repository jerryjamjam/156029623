def main():
    names = ["Mario", "Luigi", "Toad", "Yoshi"]
    for name in range(len(names)):
        print(write_letter(name, "Princess Peach"))

def write_letter(receiver, sender):
    return f"""
======================================
    Dear {receiver},

    you are hereby sentenced to death!

    SiNcEeElY,
    {sender}
=======================================
"""
main()
