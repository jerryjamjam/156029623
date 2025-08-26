people = {
    "carter": "715-123-4567",
    "david": "715-890-1234",
    "john": "715-567-8910",
}

name = input("Name: ")

if name in people:
    number = people[name]
    print (f"Found {number}")
else:
    print("not found")
