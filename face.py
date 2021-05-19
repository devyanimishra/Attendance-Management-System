

from keras.models import load_model
import pickle
import cv2
import numpy as np
from attendanceS import DB

def make_720(cap):
    cap.set(3,1280)
    cap.set(4,720)

def load_model1():      
    modelfile = 'models/opencv_face_detector_uint8.pb'
    configfile = 'models/opencv_face_detector.pbtxt'
    net = cv2.dnn.readNetFromTensorflow(modelfile, configfile)

    return net

def Detection(img):
    net = load_model1()  
    
    # HWC -> CHW
    resized = img.copy()
    input_face_img = resized.transpose([2, 0, 1])
    # CHW -> NCHW
    input_face_img = np.expand_dims(input_face_img, axis=0)
    blob = cv2.dnn.blobFromImage(resized, 1.0, (300,300), [104,117,123], False, False)
    net.setInput(blob)
    cvOut = net.forward()
    bboxes = []
    frameHeight = resized.shape[0]
    frameWidth = resized.shape[1]
    conf_threshold = 0.9
    resized1 = list()
    (h, w) = resized.shape[:2]
    for i in range(cvOut.shape[2]):
            confidence = cvOut[0, 0, i, 2]
            if confidence > conf_threshold:
                x1 = abs(int(cvOut[0, 0, i, 3] * frameWidth))
                y1 = abs(int(cvOut[0, 0, i, 4] * frameHeight))
                x2 = abs(int(cvOut[0, 0, i, 5] * frameWidth))
                y2 = abs(int(cvOut[0, 0, i, 6] * frameHeight))
                bboxes.append([x1, y1, x2, y2])
                cv2.rectangle(resized, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)), 8)
                #resized1.append(resized[y1:y2,x1:x2])
                box = cvOut[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                # extract the face ROI
                resized1.append(resized[startY:endY, startX:endX])
                for x in resized1:
                    (fH, fW) = np.asarray(x).shape[:2]
                    if fW < 20 or fH < 20:
                        continue
    
    
    return np.asarray(resized1),bboxes,resized


names = ['Alvaro_Morte','Devyani','Miguel_Herran','Pedro_Alonso','Rodrigo_de_la_Serna','Unnati','Ursula_Corbero']
model = load_model('./models/facenet_keras.h5')
present = []

def face_rec(image):
    image = cv2.resize(image, (1280, 720), interpolation=cv2.INTER_LINEAR)
    scale_percent = 96 # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
       
    face,boxes,resized = Detection(image)
    
    resized = cv2.resize(resized,dim, interpolation = cv2.INTER_AREA)
    for i in range(len(boxes)):
        out = face[i].astype('float32')
        out = cv2.resize(out, (160, 160), interpolation=cv2.INTER_LINEAR)

        #emb = Embedding(model,face)
        face_pixels = cv2.resize(out,(160,160))
        face_pixels = face_pixels.astype('float32')
            
        mean, std = face_pixels.mean(), face_pixels.std()
        face_pixels = (face_pixels - mean) / std
            
        samples = np.expand_dims(face_pixels, axis=0)
            #Face embeddings collected
        yhat = model.predict(samples)
        
        filename = 'finalized_model1.sav'
        prediction_model = pickle.load(open(filename, 'rb'))
        
        yhat_class = prediction_model.predict(yhat)
        yhat_prob = prediction_model.predict_proba(yhat)
        
        #print(yhat_class)
        class_index = yhat_class[0]
        class_probability = yhat_prob[0,class_index] * 100
        
        print(class_probability)
        print(names[class_index])
        x1,y1,x2,y2 = boxes[i]
        x1 = int(x2*scale_percent / 100)
        x2 = int(y2*scale_percent / 100)
        if(class_probability>97.5):
                    present.append(names[class_index])
                    cv2.putText(resized ,names[class_index],(x1,x2), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2,cv2.LINE_AA)
                    
        else:
            #print("Person not matched")
            cv2.putText(resized,"unknown",(x1,x2), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2,cv2.LINE_AA)
            present.append("unknown")
            
            
    return resized,present
count = 0 
def main():
    cap = cv2.VideoCapture(0)
    
    make_720(cap)
    import datetime
    
    while True:
        ret, frame = cap.read()
        stime = datetime.datetime.now()    
        resized,present = face_rec(frame)
        cv2.putText(resized,str(stime),(35,35), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),2,cv2.LINE_AA)
        cv2.imshow('frame',resized)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
               
    cap.release()
    
    cv2.destroyAllWindows()
    unique(present)
    
def unique(present):
    x  = np.array(present)
    present = np.unique(x)
    DB(present)

if __name__ == "__main__":
    main()


