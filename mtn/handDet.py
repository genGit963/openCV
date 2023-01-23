import cv2
import mediapipe as mp
import pyautogui as pag


sc_x, sc_y = pag.size()
mpHands = mp.solutions.hands # type: ignore
hands = mpHands.Hands() #for detecting hands and then tracking them.

# to draw hand landmarks
mpDraw = mp.solutions.drawing_utils #type:ignore

vdo = cv2.VideoCapture(0)

y_index = 0 
while True:
  _, frame = vdo.read()
  
  rgv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  result = hands.process(rgv) #  

  if result.multi_hand_landmarks:
    for hand_landmarks in result.multi_hand_landmarks:
      for id,lm in enumerate(hand_landmarks.landmark):
        height,width,c=frame.shape
        dx,dy=int(lm.x*width),int(lm.y*height)
        # print(dx,dy)
        if id==8:
          cv2.circle(frame,(dx,dy),9,(255,0,0),3)
          x_index = sc_x/width*dx
          y_index = sc_y/height*dy
          pag.moveTo(dx,dy)
          
        if id==4:
          cv2.circle(frame,(dx,dy),9,(255,0,0),3)
          x_indext = sc_x/width*dx
          y_indext = sc_y/height*dy
          
          if abs(y_index-y_indext)<20:
            pag.click()
          
      mpDraw.draw_landmarks(frame, hand_landmarks, mpHands.HAND_CONNECTIONS)
      
  cv2.imshow("HandDetection", cv2.flip(frame, 1))
  
  if cv2.waitKey(1) & 0xFF == ord('c'):
    break
  