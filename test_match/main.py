import pyautogui
#import cv2 # https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv
import numpy as np
from PIL import Image

def is_match(rd, fd, sx, sy, w, h):
    #print(fd[sx:w,sy:h])
    return np.array_equal(rd, fd[sy:sy+h, sx:sx+w])
    # found = True
    # for x in range(0,w):
    #     for y in range(0,h):
    #         regn_pixel = rd[y][x]
    #         full_pixel = fd[y + sy][x + sx]
    #         if not np.array_equal(full_pixel, regn_pixel):
    #             found = False
    #             #print("full_pixel={} regn_pixel={} x={} y={} sx={} sy={}".format(full_pixel, regn_pixel,x,y,sx,sy))
    #             break
    # return found


regn_x = 6
regn_y = 44

# regn_img = pyautogui.screenshot(region=[regn_x, regn_y, 64, 64]) # x,y,w,h 
regn_img = Image.open("screenshot_regn.png")
regn_data = np.asarray(regn_img)
#regn_img2 = Image.fromarray(np.uint8(regn_img))
#regn_img2.save('screenshot3.png')


# full_img = pyautogui.screenshot(region=[max(0, regn_x - 100), max(0, regn_y - 100), 200, 200]) # x,y,w,h
full_img = Image.open("screenshot_full.png")
full_data = np.asarray(full_img)
#full_img2 = Image.fromarray(np.uint8(full_img))
#full_img2.save('screenshot_full.png')

#print(regn_data[0][0])
#print(full_data[44][1])

# check_x = regn_x + 6
# check_y = regn_y - 10
check_x = 129
check_y = 194
finish = False

for x in range(0, 200):
    for y in range(0, 200):
        xdir = 1 if x % 2 == 0 else -1
        ydir = 1 if y % 2 == 0 else -1
        sx = max(0, check_x + int((x / 2) * xdir))
        sy = max(0, check_y + int((y / 2) * ydir))
        print("check sx={} sy={}".format(sx,sy))
        if is_match(regn_data, full_data, sx, sy, 64, 64):
            finish = True
            print("found sx={} sy={}".format(sx, sy))
            break
    if finish:
        break

if not finish:
    print("failed!")