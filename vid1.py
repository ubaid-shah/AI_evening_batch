import cv2

cap=cv2.VideoCapture('dog.mp4')

while True:
  ret,frame=cap.read()
  
  cv2.imshow('video of dog',frame)
  
  if cv2.waitKey(1) & 0xFF==ord('q'):
    break
  
cap.release()
cv2.destroyAllWindows()
  