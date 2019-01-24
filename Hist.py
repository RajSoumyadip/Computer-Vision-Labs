import cv2

from matplotlib import pyplot as plt

img = cv2.imread('BG.jpg',0)

histr = cv2.calcHist([img],[0],None,[256],[0,256])
cv2.imshow('input', img)
plt.plot(histr)
plt.show()

cv2.waitKey(0);
cv2.destroyAllWindows();
