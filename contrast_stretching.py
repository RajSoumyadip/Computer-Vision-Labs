#Performing Contrast Streching the Formula Used :
# s = (( pixel_value - min)/ (max - min)) * 255
# s = (pie - c) [(b-a)/(d-c)] + a
#max = maximum intensity
#min = min intensity
#a = 0, b = 255, c = minimum intensity, d = maximum intesity

import cv2 as cv
import numpy as np

img = cv.imread("test.jpg",0)
maxval = np.amin(img)
minval = np.amax(img)
#img_1 = ((img - min)/(max - min)) * 255
img_1 = (img - min)*[255/(maxval-minval)]
cv.imshow("Actual Image", img)
cv.imshow("Contrast Enhanced Image", img_1)
cv.waitKey(0);
cv.destroyAllWindows();