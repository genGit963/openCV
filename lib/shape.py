import cv2
import numpy as np
# import stackImage
import colorDetection

vdo = cv2.VideoCapture(0)

def getContours(imageCanny):
  contours, hierarchy = cv2.findContours(imageCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  return contours


  
while True:
  
  success, img = vdo.read()
  # GrayScale
  # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

  # GaussionBlur
  # blur = cv2.GaussianBlur(gray, (7,7), 1)

  # Canny:
  # canny = cv2.Canny(cv2.GaussianBlur(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), (7,7), 1),50,50)

  # blank
  # blanck = np.zeros_like(img)

  
  for cnt in getContours(cv2.Canny(cv2.GaussianBlur(cv2.cvtColor(img, cv2.COLOR_RGB2GRAY), (7,7), 1),50,50)): #arg: canny
    area = cv2.contourArea(cnt)
    # Area higher than 500
      
    if area>500:
      shape = cv2.drawContours(img, cnt, -1, (255,0,0), 4)
      colorShp = colorDetection.detect_Color(shape)
      # print("Area: ", area)
      # print("Peri: ", cv2.arcLength(cnt, True))

      cv2.imshow("Contour", colorShp)
      
  if cv2.waitKey(1) & 0xFF==ord('c'):
    break
  
# to draw contour on image
# ImageContour = img.copy()

# img = cv2.imread("images/shapes.png")


# stackShow = stackImage.stackImages(0.40,([img, gray, blur],[canny, blanck, ImageContour]))
# cv2.imshow("Grid view", stackShow)


# cv2.imshow("blur image", blur)
# cv2.imshow("Gray image", gray)
# cv2.imshow("Real Image", img)


# cv2.waitKey(0)