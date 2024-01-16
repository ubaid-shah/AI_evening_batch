import cv2

cap=cv2.VideoCapture(r'C:\Users\admin\Documents\cv_evening\haarcascade\mm.mp4')

face_cascade=cv2.CascadeClassifier(r'C:\Users\admin\Documents\cv_evening\haarcascade\haarcascade_frontalface_default.xml')

while True:
  ret,img=cap.read()

  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

  face_rec=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=9)

  for (x,y,w,h) in face_rec:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

  cv2.imshow('img',img)

  if cv2.waitKey(1) & 0xFF==ord('q'):
    break
  
    
cap.release()  
cv2.destroyAllWindows()