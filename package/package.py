class Package:
    def __init__(self, number, sender, reciever, weight):
        self.number = number
        self.sender = sender
        self.reciever = reciever
        self.weight = weight

    def __str__(self):
        return(f"{self.number} costs ${self.shipping_cost()} to ship.")

    def shipping_cost(self, cost_per_kg=.97):
        cost = self.weight * cost_per_kg
        return cost

class PackageSystem:
    def __init__(self):
        self.packages = {}

    def add_package(self, package):
        self.packages[package.number] = package
        #csv logic
        return package

    def find_package(self, number):
        return self.packages.get(number, None)

    def list_package(self):
        for package in self.packages.values():
            print(package)

def main():
    while True:
        system = PackageSystem()
        action = input("What would you like to do? 'add', 'find', 'list', 'status', 'exit' ").lower()
        if action == "add":
            number = input("number? ")
            sender = input("Sender? ")
            reciever = input("Reciever? ")
            weight = input("Weight? ")
            new_package = Package(number, sender, reciever, weight)
            system.add_package(new_package)

        elif action == "find":
            ...
        elif action == "list":
            ...
        elif action == "exit":
            ...


if __name__ == "__main__":
    main()


#ask about the os package








