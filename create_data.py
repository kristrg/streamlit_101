import numpy as np
import cv2
import time
import os

# Label 00000 la khong cam tien, con lai la cac menh gia tu nhap
label = "00000"

cap = cv2.VideoCapture(0)

# Bien de count, luu giu lieu sau 100 frame dau
i=0
while(True):
    # Capture frame by frame
    i+=1
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.resize(frame, dsize=None, fx=0.4, fy=0.4)

    # Show frame
    cv2.imshow('frame',frame)

    # Save data to folder
    if i>=100 and i<=1100:
        print("Number of photos capture = ",i-100)
        # Create folder con
        if not os.path.exists('data' + str(label)):
            os.mkdir('data' + str(label))

        cv2.imwrite('data' + str(label) + "/" + str(i) + ".png",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()