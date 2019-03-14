import cv2

img1 = cv2.imread("edge.jpg")
img2 = cv2.imread("edge1.jpg")
outimg1 = cv2.Canny(img1,threshold1 = 200, threshold2 = 300)
outimg2 = cv2.Canny(img2,threshold1 = 200, threshold2 = 300)

while(True):
    cv2.imshow('original img 1', img1)
    cv2.imshow('original img 2', img2)
    cv2.imshow('output 1', outimg1)
    cv2.imshow('output 2', outimg2)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break