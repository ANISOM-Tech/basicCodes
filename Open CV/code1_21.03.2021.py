# importing libraries
import cv2
"""
# reading image:
img = cv2.imread(r'E:\openCV projects\images\img0.jpg')

# showing image:
cv2.imshow("output image", img)

# holding the display window for infinite time 
cv2.waitKey(0)
"""
# reading video:
# cap = cv2.VideoCapture(r'E:\openCV projects\videos\videoplayback (1).mp4')

# for webcam
cap = cv2.VideoCapture(0)   # here 0 for laptop webcam
cap.set(3, 1920)     # 3 for width
cap.set(4, 1200)     # 4 for height
cap.set(10, 10)    # 10 for brightness

# isplaying video:
while True:
    success, img = cap.read()   # success contains a boolean value
    cv2.imshow('video output', img)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
