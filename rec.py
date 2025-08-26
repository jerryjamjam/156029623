def main():
    difficulty = input("Difficult or Casual? ").lower()
    players = input("Multiplayer or Singleplayer? ").lower()

    if difficulty == "difficult":
        if players == "multiplayer":
            rec("Poker")
        else:
            rec("Klondike")
    elif difficulty == "casual":
        if players == "multiplayer":
            rec("Hearts")
        else:
            rec("Clock")
    else:
        print("Choose better response")

def rec(game):
    print(f"You might like {game}")

main()
