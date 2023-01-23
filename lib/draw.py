import cv2
import numpy as np

# blanck images
blank = np.zeros((500, 500,3), dtype='uint8')
# cv2.imshow("blank", blank)

# cat image
img = cv2.imread("images/cat.jpg")
resize_img = cv2.resize(img, (0,0), fx=0.25, fy=0.25)
# cv2.imshow("Cat", resize_img)
# cv2.waitKey(0)


# cv2.rectangle(blank, (25,25), (200, 200), (0,255,0),2)
# cv2.imshow("Rectangle", blank)

# cv2.circle(resize_img, (200,200), 80, (0,255,0), 3)
# cv2.imshow("Circle", resize_img)


# # line
# cv2.line(resize_img, (30,30), (100,100), (0,0,255), 1)
# cv2.imshow("line",resize_img)

# Text on image
cv2.putText(resize_img, 'Hello Cat to Hellow World', (125,125), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
cv2.imshow("Text Written", resize_img)

cv2.waitKey(0)
cv2.destroyAllWindows()