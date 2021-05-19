import numpy as np
import cv2
import time
from matplotlib import pyplot
from os import listdir
import os
import pdb


def load_model():      
    modelfile = 'models/opencv_face_detector_uint8.pb'
    configfile = 'models/opencv_face_detector.pbtxt'
    net = cv2.dnn.readNetFromTensorflow(modelfile, configfile)

    return net


def Detection(img):
    net = load_model()  
    
    resized = img.copy()
    input_face_img = resized.transpose([2, 0, 1])
    # CHW -> NCHW
    input_face_img = np.expand_dims(input_face_img, axis=0)
    blob = cv2.dnn.blobFromImage(img, 1.0, (300,300), [104,117,123], False, False)
    net.setInput(blob)
    
    cvOut = net.forward()
    
    bboxes = []
    
    frameHeight = resized.shape[0] 
    frameWidth = resized.shape[1]
    (h, w) = resized.shape[:2]
    conf_threshold = 0.7
    for i in range(cvOut.shape[2]):
            confidence = cvOut[0, 0, i, 2]
            if confidence > conf_threshold:
                x1 = abs(int(cvOut[0, 0, i, 3] * frameWidth))
                y1 = abs(int(cvOut[0, 0, i, 4] * frameHeight))
                x2 = abs(int(cvOut[0, 0, i, 5] * frameWidth))
                y2 = abs(int(cvOut[0, 0, i, 6] * frameHeight))
                box = cvOut[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                # extract the face ROI
                resized1 = resized[startY:endY, startX:endX]
                (fH, fW) = resized1.shape[:2]
                # ensure the face width and height are sufficiently large
                if fW < 20 or fH < 20:
                    continue

                
        
    return resized1


def face(path):
    i = 1
    faces = list()
    labels = list()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(base_dir,path)
    for root,dirs,files in os.walk(image_dir):
            for file in files:
                if file.endswith("png") or file.endswith("jpg") :
                    path = os.path.join(root,file)
                    label = os.path.basename(root).replace(" ","-").lower()
                    img = cv2.imread(path)                   
                    face = Detection(img)          
                    face = cv2.resize(face, (160, 160), interpolation=cv2.INTER_LINEAR)
                    i += 1
                    faces.append(face)
                    labels.append(label)
    return faces,labels


def Dataset(path):
    X, y = list(),list()
    faces,labels = face(path)
    X.append(faces)
    y.append(labels)
    return np.asarray(X),np.asarray(y)

def main():
    path = './images1/train/'
    val = './images1/val/'
    trainX,trainy = Dataset(path)    
    testX, testy = Dataset(val)
    trainX = np.squeeze(trainX)
    trainy = np.squeeze(trainy)
    testX = np.squeeze(testX)
    testy = np.squeeze(testy)
    print(trainX.shape,trainy.shape)
    print(testX.shape,testy.shape)
    
    np.savez_compressed('face_dataset1.npz',trainX,trainy,testX, testy)

if __name__ == "__main__":
    main()


