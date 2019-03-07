import cv2
from matplotlib import pyplot as plt

img  = cv2.imread("Salt.jpg")
img_sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
img_sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_sobel),plt.title('Edge')
plt.xticks([]), plt.yticks([])
plt.show()
        