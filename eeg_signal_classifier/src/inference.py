#Created by Nicholas Smith
#credit for the original also goes to Christopher Hunter, Alex Rivera, Greg Ferdinand

#imports
from keras.models import Sequential
from keras.layers import Dense, Dropout, Bidirectional,GRU
import keras
from preprocess import PREPROCESS
from pathlib import Path
import numpy as np
import tensorflow as tf

features = ["AF3+AF4","F3+F4","F7+F8","AF3-O2","F3-P8","F7-T8","FC5+FC6","O1+O2","P7+P8","T7+T8","AF3*AF4","F3*F4","F7*F8","FC5*FC6","O1*O2","P7*P8","T7*T8","AF3","AF4","F3","F4","F7","F8","FC5","FC6","O1","O2","P7","P8","T7","T8"]

feature_flag = 1 #used for determining the number of columns needed for building the model

k_timesteps = 73 #k is the number of rows to use meaning how many time steps of EEG activity to map to a single game label
train_partition=.9 #train-test split
scaling_mode = 1 #scaling mode
dataset_proportion = 1 #percent of dataset to use 
use_pca = False #use PCA flag
pca_components = 30 #if using PCA, number of top principal components to use
num_columns = 31
    
#apply feature creation/selection, scale data, perform PCA if selected, and get train-test split 
_, _, X_test, y_test = PREPROCESS(k_timesteps, train_partition, dataset_proportion, scaling_mode, use_pca, pca_components,features)

X_test,y_test = np.array(X_test),np.array(y_test)
#onehot encode labels
y_test = tf.keras.utils.to_categorical(y_test, num_classes = 4)
#reshape data to work with tf/keras
X_test_shape=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],X_test.shape[2]))

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

#run model on test set
results = model.evaluate(X_test, y_test, batch_size=32)
print("Test accuracy:",results[1])

