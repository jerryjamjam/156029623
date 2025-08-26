import emoji

def main():
    while True:
        emoji_input = input("Input: ").strip()
        emoji_output = emoji.emojize(emoji_input, language='alias')
        print(f"Output: {emoji_output}")
        break
main()


































