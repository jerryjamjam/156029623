def main():
    amount_due = 50
    while True:
        coin_in = int(input("Insert Coin: "))
        if coin_in in [25, 10, 5]:
            amount_due -= coin_in
            print(f"Amount Due: {amount_due}")
            if amount_due <= 0:
                print(f"Change Owed: {abs(amount_due)}")
                break
        else:
            print("Amount Due: 50")
            break
main()


