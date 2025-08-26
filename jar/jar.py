class Jar:
    def __init__(self, capacity):
        self.capacity = capacity

    def __str__(self):
        #print the number of cookies but use emojis instead
        ...
    def deposit(self, n):
        #add cookies to the jar
        ...

    def withdraw(self):
        #subtract cookies from the jar
        ...

    @property
    def capacity(self):
        #will return the capacity
        ...
    @property
    def size(self):
        #will keep track of the size
        ...

def main():
    ...

if __name__ == "__main__":
    main()
