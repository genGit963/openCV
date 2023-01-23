import cv2 as cv
import numpy as np

img = cv.imread("images/objects.jpg")

# normal resize picture
img_resize = cv.resize(img, (0,0), fx=0.20, fy=0.20)
cv.imshow("Baby", img_resize)


# Converting to grayScale
# gray = cv.cvtColor(img_resize, cv.COLOR_BGR2GRAY)
# cv.imshow("gray-scale", gray) 

# Gaussion Blur Effect 
blur = cv.GaussianBlur(img_resize, (1,1), cv.BORDER_DEFAULT)
# cv.imshow("Blur Effect", blur)

# Edge Cascade of img_resize
canny = cv.Canny(img_resize, 125, 180)
# cv.imshow("Canny", canny)


# Edge Cascade of blur image
canny_blur= cv.Canny(blur, 105, 100)
# cv.imshow("Canny_blur", canny_blur)

# dilate the img
dilate = cv.dilate(canny, (5,5),7)

# resizing and cropping images
cropped = img_resize[20:300,  40: 500]
cv.imshow("Cropped", cropped)


# joint = np.hstack((canny_blur,dilate,canny))
# cv.imshow("joint", joint)

cv.waitKey(0)
cv.destroyAllWindows()