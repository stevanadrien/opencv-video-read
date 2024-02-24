import cv2 as cv
path = 'CV/example.mp4'
capture = cv.VideoCapture(path)
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()