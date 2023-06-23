import cv2 as cv
img = cv.imread("Gunja Sign.jpg")
cv.imshow('window', img)
cv.imwrite('Gunja Sign.jpg', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite("GunjaSignGray.jpg", gray)
cv.imshow('window1', gray)
cv.waitKey(0)
cv.destroyAllWindows()