
import numpy as np
from keras.models import load_model


def Embedding(model, face_pixel):
    face_pixel = face_pixel.astype('float32')
    mean, std = face_pixel.mean(), face_pixel.std()
    face_pixel =(face_pixel-mean)/std
    samples = np.expand_dims(face_pixel, axis = 0)
    yhat = model.predict(samples)
    return yhat[0]

def main():
    data = np.load('face_dataset1.npz')
    trainX, trainY, testX, testY = data['arr_0'], data['arr_1'], data['arr_2'], data['arr_3']
    print(trainX.shape, trainY.shape, testX.shape, testY.shape) 
    
    model = load_model('./models/facenet_keras.h5')
    
    
    newTrainX = list()
    newTestX = list()
    for face_pixel in trainX:
        embedding = Embedding(model,face_pixel)
        newTrainX.append(embedding)
    
    newTrainX = np.asarray(newTrainX)
    print(newTrainX.shape)
    
    for face_pixel in testX:
        embedding = Embedding(model,face_pixel)
        newTestX.append(embedding)
        
    newTestX = np.asarray(newTestX)
    print(newTestX.shape)
    np.savez_compressed('face-embedding1.npz', newTrainX, trainY, newTestX, testY)

if __name__ == "__main__":
    main()