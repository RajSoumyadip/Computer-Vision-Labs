import cv2
from matplotlib import pyplot as plt

img  = cv2.imread("edge.jpg")
outimg = cv2.Canny(img,threshold1 = 200, threshold2 = 300)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(outimg),plt.title('Edge')
plt.xticks([]), plt.yticks([])
plt.show()
        