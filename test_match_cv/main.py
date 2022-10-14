import time

import cv2
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
#读取图像

GLOBAL_W = 64
GLOBAL_H = 64
GLOBAL_HALF_W = int(GLOBAL_W/2)
GLOBAL_HALF_H = int(GLOBAL_H/2)

def img_show(title, img):
    cv2.namedWindow('title', 0)  # 0 or CV_WINDOW_AUTOSIZE(default）
    cv2.imshow('title', img)
    cv2.waitKey(0)  # 0 or positive value(ms)
def check_color(full_img, regn_img):
    regn_data = cv2.cvtColor(regn_img, cv2.COLOR_BGR2RGB)
    full_data = cv2.cvtColor(full_img, cv2.COLOR_BGR2RGB)
    diff_num = 0;
    for x in range(0, GLOBAL_W):
        for y in range(0, GLOBAL_H):
            regn_pixel = regn_data[x, y]
            full_pixel = full_data[x, y]
            diff_r = int(full_pixel[0]) - int(regn_pixel[0])
            diff_g = int(full_pixel[1]) - int(regn_pixel[1])
            diff_b = int(full_pixel[2]) - int(regn_pixel[2])
            DIFF = 20
            if abs(diff_r) > DIFF or abs(diff_g) > DIFF or abs(diff_b) > DIFF:
                ++diff_num
    return diff_num < (GLOBAL_W * GLOBAL_H) * 0.1

img1 = cv2.imread('match_full.png', 0)
img2 = cv2.imread('match_regn.png', 0)

print(type(img1))

start_time = time.perf_counter_ns()
#使用sift算法，计算特征向量与特征点
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)


if len(kp1) or len(kp2) == 0:
    print(check_color(img1, img2))
    exit(0)

# crossCheck表示两个特征点要互相匹，例如A中的第i个特征点与B中的第j个特征点最近的，并且B中的第j个特征点到A中的第i个特征点也是
#NORM_L2: 归一化数组的(欧几里德距离)，如果其他特征计算方法需要考虑不同的匹配计算方式
bf = cv2.BFMatcher(crossCheck=True)
matches = bf.match(des1, des2)
use_time = time.perf_counter_ns() - start_time
print(use_time)


#对点的距离的排序
matches = sorted(matches, key=lambda x: x.distance)
print(matches[0].distance)

match_desc = kp1[matches[0].queryIdx].pt
print(match_desc)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None,flags=2)
#图片展示

img_show('img3',img3)
