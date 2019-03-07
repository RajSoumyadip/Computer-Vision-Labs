import cv2
from matplotlib import pyplot as plt

img  = cv2.imread("edge.jpg")
blur_img = cv2.GaussianBlur(img,(5,5),0)
img_sobelx = cv2.Sobel(blur_img,cv2.CV_64F,1,0,ksize=5)
img_sobely = cv2.Sobel(blur_img,cv2.CV_64F,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely

plt.subplot(121),plt.imshow(blur_img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_sobel),plt.title('Edge Detection after GD')
plt.xticks([]), plt.yticks([])
plt.show()