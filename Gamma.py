import cv2 as cv
import numpy as np

img_1 = cv.imread("img.jpg",0)

gmma = 2
img_2 = np.power(img_1,gmma)

gmma = 0.45
img_3 = np.power(img_1,gmma)

gmma = 8
img_4 = np.power(img_1,gmma)

cv.imshow('input input', img_1)
cv.imshow('gmma 2', img_2)
cv.imshow('gmma 3', img_3)
cv.imshow('gmma 4', img_4)
cv.waitKey(0);
cv.destroyAllWindows();
