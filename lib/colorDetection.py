import cv2
import numpy as np

# cv2.imshow("cat",img)

def empty(arg):
  pass

def detect_Color(importImage):
  # creating scale for HSV
  cv2.namedWindow("TrackBar")
  cv2.resizeWindow("TrackBar", 640,400)

  # human color filter: (HMn,HMx,SMn,SMx,VMn,VMx): 26, 56, 0, 212, 0, 218

  cv2.createTrackbar("Hue Min","TrackBar", 26,179,empty)
  cv2.createTrackbar("Hue Max","TrackBar", 56,179,empty)

  cv2.createTrackbar("Sat Min","TrackBar", 0,255,empty)
  cv2.createTrackbar("Sat Max","TrackBar", 212,255,empty)

  cv2.createTrackbar("Val Min","TrackBar", 0,255,empty)
  cv2.createTrackbar("Val Max","TrackBar", 218,255,empty)

  # get trackbar positions
  # vdo = cv2.VideoCapture(0)
  while True:
    # success,img=vdo.read()
    img = importImage
    # imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    HMn = cv2.getTrackbarPos("Hue Min", "TrackBar")
    HMx = cv2.getTrackbarPos("Hue Max", "TrackBar")
    SMn = cv2.getTrackbarPos("Sat Min", "TrackBar")
    SMx = cv2.getTrackbarPos("Sat Max", "TrackBar")
    VMn = cv2.getTrackbarPos("Val Min", "TrackBar")
    VMx = cv2.getTrackbarPos("Val Max", "TrackBar")
    
    print(HMn,HMx,SMn,SMx,VMn,VMx)
    
    lower = np.array([HMn, SMn, VMn])
    upper = np.array([HMx, SMx, VMx])
    
    # Masking
    masked = cv2.inRange(img,lower,upper)
    detection = cv2.bitwise_and(img, img, mask=masked)
    
    # cv2.imshow("Normal ", img)
    # cv2.imshow("HSV", imgHSV)
    # cv2.imshow("maskedImg", masked)
    # cv2.imshow("Detected", detection)
    
    
    # if cv2.waitKey(1) & 0xFF == ord('c'):
    #   break
    
    return detection


# hsv image

