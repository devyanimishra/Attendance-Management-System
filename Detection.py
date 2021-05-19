
from __future__ import division
import cv2
import sys
import numpy as np
import datetime


def Detectface(frame):
    
    modelfile = 'models/opencv_face_detector_uint8.pb'
    configfile = 'models/opencv_face_detector.pbtxt'
    net = cv2.dnn.readNetFromTensorflow(modelfile, configfile)

    conf_threshold = 0.7
    framednn = frame.copy()
    frameheigth = framednn.shape[0]
    print(frameheigth)
    framewidth = framednn.shape[1]
    
    blob = cv2.dnn.blobFromImage(framednn, 1.0, (300,300), [104,117,123], False, False)
    
    net.setInput(blob)
    detection = net.forward()
    boxes = []

    for i in range(detection.shape[2]):
        confidence = detection[0, 0, i, 2]
        
        if confidence > conf_threshold:
            x1 = int(detection[0, 0, i, 3] * framewidth)
            y1 = int(detection[0, 0, i, 4] * frameheigth)
            x2 = int(detection[0, 0, i, 5] * framewidth)
            y2 = int(detection[0, 0, i, 6] * frameheigth)    
            boxes.append([x1,y1,x2,y2])          
        
    return framednn,boxes


def main(path):
    cap = cv2.VideoCapture(0)
    i=0
    while True:
        ret, frame = cap.read()
        
        outframednn, boxes = Detectface(frame)
        cv2.putText(outframednn,str(i),(160,160),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow('frame',outframednn)
        if len(boxes) != 0 :
            if cv2.waitKey(20) & 0xFF == ord('s'):
                print("hello",i)
                cv2.imwrite('C:/Python 3.6/MPR/img/Train/'+path+'/'+str(i)+'.jpg',frame)
                cv2.imwrite('C:/Python 3.6/MPR/img/val/'+path+'/'+str(i)+'.jpg',frame)
                i += 1
                continue
        
        if cv2.waitKey(20) & 0xFF == ord('q') or i==6:
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main(path)