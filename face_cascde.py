import cv2

img=cv2.imread(r'C:\Users\admin\Documents\cv_evening\haarcascade\m.jpg')

face_cascade=cv2.CascadeClassifier(r'C:\Users\admin\Documents\cv_evening\haarcascade\haarcascade_frontalface_default.xml')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_rec=face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=9)

for (x,y,w,h) in face_rec:
  cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()