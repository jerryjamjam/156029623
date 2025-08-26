from PIL import Image
import sys
import string

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    if not sys.argv[1].endswith(".jpg") or not sys.argv[2].endswith("jpg"):
        print("Invalid output")
        sys.exit(1)
    if sys.argv[1].split(".")[-1] != sys.argv[2].split(".")[-1]:
        print("Input and output have different extensions")
        sys.exit(1)

    try:
        with Image.open("shirt.png") as img:
            with Image.open(sys.argv[1]) as img2:
                resizedimg = img.resize((1200, 1600), Image.Resampling.NEAREST)
                x = int((img2.width - resizedimg.width) // 2)
                y = int((img2.height - resizedimg.height) // 2)
                img2.paste(resizedimg, (x,y - 110), resizedimg)
                crop = (0, 0, resizedimg.width, resizedimg.height - 110)
                croppedimg2 = img2.crop(crop)
                croppedimg2.save(sys.argv[2])

    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()



