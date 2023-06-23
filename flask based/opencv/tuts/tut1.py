import cv2 as cv

img = cv.imread("Gunja Sign.jpg")
cv.imshow('window', img)

cv.waitKey(0)
cv.destroyAllWindows()