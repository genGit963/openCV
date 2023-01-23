import cv2

# vdo 

vdo = cv2.VideoCapture(0)

while True:
  success, frame = vdo.read()
  img = cv2.flip(frame, 1) #flip vetically
  
  cv2.imshow("Painting", img)
  
  if cv2.waitKey(1) & 0xFF == ord('c'):
    break
