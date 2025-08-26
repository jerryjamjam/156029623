class Vault:
    def __init__(self, gallions=0, sickles=0, kenucks=0):
        self.gallions = gallions
        self.sickles = sickles
        self.kenucks = kenucks

    def __str__(self):
        return f"together they have {self.gallions}!!!"

    def __add__(self, other):
        gallions = self.gallions + other.gallions
        return Vault(gallions)

potter = Vault(100, 50, 25)
print(f"potter has {potter.gallions}!!")

weasley = Vault(120, 3, 200)
print(f"weasley has {weasley.gallions}!!!")

total = potter + weasley
print(total)




