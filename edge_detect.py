import cv2
import numpy as np

img=cv2.imread('fruits.jpg')

img_ed=cv2.Canny(img,100,200)

dilat_img=cv2.dilate(img_ed,np.ones((3,3)))
erode_img=cv2.erode(dilat_img,np.ones((3,3)))

cv2.imshow('fruit',img)
cv2.imshow('fruit img_ed',img_ed)
cv2.imshow('dilat_img',dilat_img)
cv2.imshow('erode_img',erode_img)
cv2.waitKey(0)
cv2.destroyAllWindows()