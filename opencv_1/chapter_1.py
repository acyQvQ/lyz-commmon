import cv2
import numpy as np

img = cv2.imread("opencv/laoba.jpg")
kernel = np.ones((5, 5), np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binaryImg = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)
imgBlur = cv2.GaussianBlur(binaryImg, (3, 3), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
cv2.imshow("Gray Image", binaryImg)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.waitKey(0)
