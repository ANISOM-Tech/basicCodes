import cv2

img = cv2.imread(r'E:\openCV projects\images\img5.jpg')

# RGB to Gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur
img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0.75)

# Canny edge detector
img_canny = cv2.Canny(img, 100, 150)

cv2.imshow('original image', img)
cv2.imshow('gray scale image', img_gray)
cv2.imshow('blur image', img_blur)
cv2.imshow('edge', img_canny)
cv2.waitKey(0)