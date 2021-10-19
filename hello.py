import yaml
from datetime import datetime
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import numpy as np
import matplotlib.pyplot as plt
def yaml1(i):
    with open('new.yaml') as f:
    
        docs = yaml.load_all(f, Loader=yaml.FullLoader)
    
        for doc in docs:
            
            for key, value in doc.items():
                valu = value[0:i]	
    return valu
# load data
def modeltrain(num_classes,num_pixels,i):
    model = Sequential()
    model.add(Dense(num_pixels, input_dim=num_pixels, kernel_initializer='normal', activation='relu'))
    model.add(Dense(num_classes, kernel_initializer='normal', activation='relu'))
    value=yaml1(i)
    for i in value:
        exec(i)
    #model.add(Dense(num_classes, kernel_initializer='normal', activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
    return model
def loaddata():
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    num_pixels = X_train.shape[1] * X_train.shape[2]
    X_train = X_train.reshape((X_train.shape[0], num_pixels)).astype('float32')
    X_test = X_test.reshape((X_test.shape[0], num_pixels)).astype('float32')
    X_train = X_train / 255
    X_test = X_test / 255
    y_train = np_utils.to_categorical(y_train)
    y_test = np_utils.to_categorical(y_test)
    num_classes = y_test.shape[1]
    i=0
    for i in range(5):
        model=modeltrain(num_classes,num_pixels,i)
        model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=5, batch_size=200, verbose=2)
        scores = model.evaluate(X_test, y_test, verbose=1)
        print("Baseline Error: %.2f%%" % (100-scores[1]*100))
        test_loss, test_acc = model.evaluate(X_test, y_test)
        print('Test loss', test_loss)
        print('Test accuracy', test_acc)
        with open('Output.txt', 'a') as f:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("date and time ",dt_string,file=f)	
            print(test_acc, file=f)
        if test_acc < 0.95:
            continue
        else:
            break


loaddata()
 
        



				