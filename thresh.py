import cv2

img=cv2.imread('bear.jpg')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(img_gray,128,255,cv2.THRESH_BINARY)
ret,thresh80=cv2.threshold(img_gray,80,255,cv2.THRESH_BINARY)
blur=cv2.blur(thresh80,(11,11))
ret,threshblur=cv2.threshold(blur,80,255,cv2.THRESH_BINARY)


cv2.imshow('bear',img_gray)
cv2.imshow('thresh',thresh)
cv2.imshow('thresh80',thresh80)
cv2.imshow('threshblur',threshblur)


cv2.waitKey(0)
cv2.destroyAllWindows()