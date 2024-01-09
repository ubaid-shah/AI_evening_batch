import cv2

img=cv2.imread('cow-salt-peper.png')
img=cv2.resize(img,(500,332))

img_blur=cv2.blur(img,(7,7))
g_blur=cv2.GaussianBlur(img,(7,7),0)
m_blur=cv2.medianBlur(img,7)
b_blur=cv2.bilateralFilter(img,9,75,75)

cv2.imshow('cow',img)
cv2.imshow('cow blur',img_blur)
cv2.imshow('cow gblur',g_blur)
cv2.imshow('cow mblur',m_blur)
cv2.imshow('cow b_blur',b_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()