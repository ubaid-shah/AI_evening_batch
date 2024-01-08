import cv2
img=cv2.imread(r'C:\Users\admin\Documents\cv_evening\coca-cola-logo.png')
img_r=cv2.resize(img,(350,350))
img_r_g=cv2.cvtColor(img_r,cv2.COLOR_BGR2GRAY)
cv2.imwrite('coke_gray.jpg',img_r_g)

# cv2.imshow('coca cola',img)
# cv2.imshow('chota coke',img_r)
# cv2.imshow('chota coke Gray',img_r_g)
# cv2.waitKey(0)
cv2.destroyAllWindows()