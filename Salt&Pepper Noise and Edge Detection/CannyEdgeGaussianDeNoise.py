import cv2
from matplotlib import pyplot as plt

img  = cv2.imread("Salt.jpg", 1)
blur_img = cv2.GaussianBlur(img,(5,5),0)
outimg = cv2.Canny(blur_img,threshold1 = 50, threshold2 = 150)

plt.subplot(121),plt.imshow(blur_img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(outimg),plt.title('Canny Edge After Gaussian Denoise')
plt.xticks([]), plt.yticks([])
plt.show()
        