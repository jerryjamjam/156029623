from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("in.jpeg") as img
        print(img.size)
        print(img.format)
        img = img.rotate(180)
        img = img.Filter(ImageFilter.BLUR) #can also use .FIND_EDGES....F***
        img.save("out.jpeg)

main()
