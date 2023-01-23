import cv2

vdo = cv2.VideoCapture(0)
while True:
  success, frame = vdo.read()
  faceCascade = cv2.CascadeClassifier("images/haarcascade_frontalface_default.xml")
  img = cv2.flip(frame, 1)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
  # faces
  faces = faceCascade.detectMultiScale(gray, 1.1, 4)
  
  # for select face
  
  for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)
    
  
  cv2.imshow("faceDetection", img)  
  if cv2.waitKey(1) & 0xFF == ord('c'):
    break