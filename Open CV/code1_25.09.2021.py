# Reading images and videos
import cv2 as cv


# Reading images
# img = cv.imread(r'E:\openCV projects\images\img5.jpg')
# cv.imshow('image', img)
#
# cv.waitKey(0)

# Reading videos
capture = cv.VideoCapture(r'E:\openCV projects\videos\videoplayback (1).mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        print(cv.waitKey(20))
        print(ord('d'))
        break

capture.release()
cv.destroyAllWindows()