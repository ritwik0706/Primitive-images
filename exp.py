# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 01:10:01 2019

@author: Ritwik
"""


""" 
Used to learn numpy and to do expirements on numpy
"""

import cv2
import numpy as np
import random

img = cv2.imread("monalisa.jpg")
resized_image = cv2.resize(img, (256, 256))
shape = (5, 5, 3)

img1 = np.random.randint(0, 256, img.shape , dtype = np.uint8)
outpath = "D:/Programming/Projects/GA/Primitive Images/Best/out.jpg"
cv2.imwrite(outpath, img1)

dif_sq = np.square(img-img1, dtype = np.int32)
sum_di_sq = np.sum(dif_sq)

img2 = np.random.randint(0, 256, (5,5,3) , dtype = np.uint8)
tp = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

img2[:] = tp

cv2.imshow('Random', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


ls = np.random.randint(0, 5, (4,4,2) , dtype = np.int32)
ls1 = np.divide(ls, np.sum(ls))
ls2 = np.random.randint(0, 5, (4,4,2) , dtype = np.int32)

bl = ls==ls2

s = np.sum(bl)
n = np.count_nonzero(bl)

for i in range(0,5, 2):
	if i+2 <= 4 :		
		for j in range(0, 5, 2):
			if j+2 <= 4:
				target = ls[i:i+2,j:j+2]
				print(target)
				
tp = np.random.randint(0, 256, (4, 3) , dtype = np.uint8)
tp[:] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

is_mutate = np.random.randint(0, 2, size=(4,4), dtype=np.bool) < 0.1
sh = ls[is_mutate].shape
ls[is_mutate] = np.random.randint(0, 5, size=sh, dtype=np.uint8)

m = [1, 2, 5, 3, 4]
ind = np.argmax(m)

img = np.random.randint(0, 256, (256,256,3) , dtype = np.uint8)
tp = [random.randint(0,256), random.randint(0,256), random.randint(0,256)]
img[:] = tp

a = np.array([[1,2], [2,3]])
counts = np.bincount(a)
x = np.argmax(counts)

noise = cv2.imread("noise.jpg")

kernel = np.ones((15, 15), np.float32)/225
smoothed = cv2.filter2D(noise, -1, kernel)

blur = cv2.GaussianBlur(noise, (15, 15), 0)
median = cv2.medianBlur(noise, 15)
bilateral = cv2.bilateralFilter(noise, 15, 75, 75)

cv2.imshow('Random', median)
cv2.waitKey(0)
cv2.destroyAllWindows()