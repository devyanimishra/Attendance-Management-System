

import numpy as np
from random import choice
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC 
import pickle

def training():
    data = np.load('face-embedding1.npz')
    trainX, trainY, testX, testY = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']

    testX_faces = data['arr_2']
    
    encoder = Normalizer(norm='l2')
    trainX = encoder.transform(trainX)
    testX = encoder.transform(testX)
    
    label_encoder = LabelEncoder()
    label_encoder.fit(trainY)
    trainY = label_encoder.transform(trainY) 
    testY =  label_encoder.transform(testY)
    
    model = SVC(C=1.0,kernel = 'linear', probability = True,class_weight='balanced')
    print(model)
    model.fit(trainX,trainY)
    
    filename = 'finalized_model1.sav'
    pickle.dump(model, open(filename, 'wb'))

if __name__ == "__main__":
    training()

