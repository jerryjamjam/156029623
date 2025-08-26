def main():
    spacecraft = {
        "name": "Voyager 1", "distance": 163
    }
    spacecraft.update({"distance": .01, "orbit": "sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ======= REPORT =======

        Name: {spacecraft["name"]}
        Distance: {spacecraft["distance"]} AU
        Orbit: {spacecraft["orbit"]}

    ======================
    """
main()


distances = {
    "voyager 1": 163
}
def main():
    for name in distances.keys():
        print(f"{name} is {distances[name] away from earth"})
main()
