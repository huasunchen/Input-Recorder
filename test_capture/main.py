import pyautogui
#import cv2 # https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv
import numpy as np
from PIL import Image

img = pyautogui.screenshot(region=[0, 0, 1920, 1080]) # x,y,w,h
img_data = np.asarray(img)
print(img_data.tobytes())

img = Image.fromarray(np.uint8(img))
img.save('screenshot3.png')
#img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR) # cvtColor用于在图像中不同的色彩空间进行转换,用于后续处理。
#cv2.imwrite('screenshot3.jpg', img)
