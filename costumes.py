import sys

import PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    image.append(image)

images[0].save("constume.gif", save_all=True, append_images=(images[1], duration=200, loop=0))
