import cv2
img=cv2.imread('coca-cola-logo.png')

# Draw Line
cv2.line(img,(0,0),(350,350),(255,178,102),2)
cv2.line(img,(0,350),(350,350),(255,255,102),2)

# Draw Circle
cv2.circle(img,(350,350),50,(0,255,0),2)
cv2.circle(img,(450,450),50,(0,255,0),-1)

# Draw Rectangle
cv2.rectangle(img,(200,200),(400,300),(255,0,0),2)
cv2.rectangle(img,(400,100),(700,200),(255,0,255),-1)

# Put text on Image
cv2.putText(img,'Thanda Matlab Coca Cola',(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(204,255,229),2)

cv2.imshow('coke',img)
cv2.waitKey(0)
cv2.destroyAllWindows()