#Created by Nicholas Smith, Christopher Hunter, Alex Rivera, Greg Ferdinand, Chih-Lun Kang

#imports
from keras.models import Sequential
from keras.layers import Dense, Dropout, Bidirectional,GRU
import keras
import pickle

#load X_test and y_test using pickle

#saved preprocessed test set from the train-validation-test split used to 
#train the model; model has not seen the test set
with open('X_test.pkl', 'rb') as f:
    X_test = pickle.load(f)
with open('y_test.pkl', 'rb') as f:
    y_test = pickle.load(f)

#time-steps k
k = 73
#number of features used (includes 17 custom features)
num_columns = 31

#define model as originally trained
model = Sequential()
model.add(keras.Input(shape=(k,num_columns)))
model.add(Bidirectional(GRU(units=146,return_sequences=True,activation='tanh')))
model.add(Dropout(.3))
model.add(Bidirectional(GRU(units=146,activation='tanh')))
model.add(Dropout(.4))
model.add(Dense(73,activation='tanh'))
model.add(Dropout(.5))
model.add(Dense(4,activation="softmax"))

#compile model
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

#load weights from prervious training
model.load_weights("model_weights.weights.h5")

#run model on test set
results = model.evaluate(X_test, y_test, batch_size=32)
print("Test accuracy:",results[1])

