from PIL import Image
import numpy as np

im = Image.open("screenshot3.png")
print(im.getpixel((22, 22)))

