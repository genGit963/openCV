import cv2 as cv

img = cv.resize(cv.imread("images/cat.jpg"), (0, 0), fx=0.20, fy=0.20)
cv.imshow("cat", img)

cv.waitKey(0)