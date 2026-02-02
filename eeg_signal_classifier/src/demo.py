#Created by Nicholas Smith
#credit for the original also goes to Christopher Hunter, Alex Rivera, Greg Ferdinand

#imports
from keras.models import Sequential
from keras.layers import Dense, Dropout, Bidirectional,GRU
import keras
from preprocess import PREPROCESS
import pickle
from pathlib import Path
import numpy as np
import os

#load X_test and y_test using pickle

sample_path = os.path.join(os.path.dirname(__file__), "..", "data", "sample.pkl")

with open(sample_path, 'rb') as f:
    sample = pickle.load(f)

X_test, y_test = sample

k_timesteps = 73 #k is the number of rows to use meaning how many time steps of EEG activity to map to a single game label
num_columns = 31
    
#define model as originally trained
model = Sequential()
model.add(keras.Input(shape=(k_timesteps,num_columns)))
model.add(Bidirectional(GRU(units=146,return_sequences=True,activation='tanh')))
model.add(Dropout(.3))
model.add(Bidirectional(GRU(units=146,activation='tanh')))
model.add(Dropout(.4))
model.add(Dense(73,activation='tanh'))
model.add(Dropout(.5))
model.add(Dense(4,activation="softmax"))

#compile model
model.compile(optimizer=None,loss='categorical_crossentropy',metrics=['accuracy'])

#load weights from prervious training
MODEL_DIR = Path(__file__).parent / "model"
checkpoint_path = MODEL_DIR / "model_weights.weights.h5"
model.load_weights(checkpoint_path)

print("Predicting video game genre based on EEG timeseries input...")
print()

#run model on samples
results = np.argmax(model.predict(X_test),axis=1) + 1
y_test = np.argmax(y_test,axis = 1) + 1

print()
for idx in range(5):
    print("Sample #"+str(idx+1)+": Game genre: " +str(y_test[idx]) + "; predicted genre: "+str(results[idx]))

    

