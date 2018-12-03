import numpy as np
import cv2
import time

#import the cascade for face detection
#face_cascade = cv2.CascadeClassifier('cascadedetect.xml')
face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
def TakeSnapshotAndSave():
    # access the webcam (every webcam has a number, the default is 0)
    cap = cv2.VideoCapture(0)

    num = 0 
    #while num<10:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # to detect faces in video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imwrite('opencv'+str(num)+'.jpg',frame)
            num = num+1
            time.sleep(.5)
            
        cv2.imshow('Video', frame)
            # roi_gray = gray[y:y+h, x:x+w]
            #roi_color = frame[y:y+h, x:x+w]

        #x = 0
        #y = 20
        #text_color = (0,255,0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #cv2.imwrite('opencv'+str(num)+'.jpg',frame)
        #num = num+1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    TakeSnapshotAndSave()