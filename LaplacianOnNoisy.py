import cv2

img10 = cv2.imread("edge.jpg")
img20 = cv2.imread("log.jpg")
depth = cv2.CV_32F
kernel = 3
img1 = cv2.GaussianBlur(img10, (5,5), 1)
img2 = cv2.GaussianBlur(img20, (3,3), 1)

outimg1 = cv2.Laplacian(img1, depth)
outimg2 = cv2.Laplacian(img2, depth)
abs_dst1 = cv2.convertScaleAbs(outimg1)
abs_dst2 = cv2.convertScaleAbs(outimg2)

while(True):
    cv2.imshow('original img 1', img1)
    cv2.imshow('original img 2', img2)
    cv2.imshow('output 1', abs_dst1)
    cv2.imshow('output 2', abs_dst2)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break