#Videp capture
import cv2 as cv
cap = cv.VideoCapture(0)
while True:
    #capture frame by frame
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    #display the result
    cv.imshow('window', frame)
    if cv.waitKey(0) & 0xFF == ord('q'):
        break

    cap.release()
    cv.destroyAllWindows()

    #  NHA_UM_00579132
