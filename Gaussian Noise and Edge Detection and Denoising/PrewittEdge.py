import cv2
from matplotlib import pyplot as plt
import numpy as np

img  = cv2.imread("edge.jpg")

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img, -1, kernelx)
img_prewitty = cv2.filter2D(img, -1, kernely)
img_prewitt = img_prewittx+img_prewitty

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_prewitt),plt.title('Edge')
plt.xticks([]), plt.yticks([])
plt.show()