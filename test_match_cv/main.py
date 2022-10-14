import time

import cv2
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
#读取图像

def img_show(title, img):
    cv2.namedWindow('title', 0)  # 0 or CV_WINDOW_AUTOSIZE(default）
    cv2.imshow('title', img)
    cv2.waitKey(0)  # 0 or positive value(ms)

img1 = cv2.imread('match_full.png', 0)
img2 = cv2.imread('match_regn.png', 0)
start_time = time.perf_counter_ns()
#使用sift算法，计算特征向量与特征点
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)


print(len(kp1))
print(len(kp2))
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
