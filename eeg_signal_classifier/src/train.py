#Created by Nicholas Smith
#credit for the original also goes to Christopher Hunter, Alex Rivera, Greg Ferdinand

###############################################################################
#imports
import keras
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Sequential
from preprocess import PREPROCESS
from keras.layers import Dense, Dropout, Bidirectional, GRU
import os, time
from pathlib import Path

#all normal EEG channels: "AF3","AF4","F3","F4","F7","F8","FC5","FC6","O1","O2","P7","P8","T7","T8"

features = ["AF3+AF4","F3+F4","F7+F8","AF3-O2","F3-P8","F7-T8","FC5+FC6","O1+O2","P7+P8","T7+T8","AF3*AF4","F3*F4","F7*F8","FC5*FC6","O1*O2","P7*P8","T7*T8","AF3","AF4","F3","F4","F7","F8","FC5","FC6","O1","O2","P7","P8","T7","T8"]

feature_flag = 1 #used for determining the number of columns needed for building the model

k_timesteps = 73 #k is the number of rows to use meaning how many time steps of EEG activity to map to a single game label
train_partition=.9 #train-test split
validation_partition = 1/9 #validation split
scaling_mode = 1 #scaling mode
dataset_proportion = 1 #percent of dataset to use 
use_pca = False #use PCA flag
pca_components = 30 #if using PCA, number of top principal components to use

#determine number of columns
if feature_flag==1 and use_pca==False:
    num_columns = len(features)
elif feature_flag==1 and use_pca==True:
    num_columns = pca_components
else:
    num_columns=14
    
#apply feature creation/selection, scale data, perform PCA if selected, and get train-test split 
X_train,y_train,X_test,y_test = PREPROCESS(k_timesteps, train_partition, dataset_proportion, scaling_mode, use_pca, pca_components,features)

#convert to numpy format
X_train,X_test,y_train,y_test = np.array(X_train),np.array(X_test),np.array(y_train),np.array(y_test)

#onehot encode labels
y_train = tf.keras.utils.to_categorical(y_train, num_classes = 4)
y_test = tf.keras.utils.to_categorical(y_test, num_classes = 4)

#reshape data to work with tf/keras
X_train_shape=np.reshape(X_train,(X_train.shape[0],X_train.shape[1],X_train.shape[2]))
X_test_shape=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],X_test.shape[2]))

#make validation split
length = round(len(X_train)*validation_partition)
X_train,y_train,X_val,y_val = X_train[length:],y_train[length:],X_train[:length],y_train[:length]

#print out training, testing, and validation partition lengths
print("X_train length:",len(X_train))
print("X_val length:",len(X_val))
print("X_test length:",len(X_test))
print("y_train length:",len(y_train))
print("y_val length:",len(y_val))
print("y_test length:",len(y_test))

###############################################################################
#define model
model = Sequential()
model.add(keras.Input(shape=(k_timesteps,num_columns)))
model.add(Bidirectional(GRU(units=146,return_sequences=True,activation='tanh')))
model.add(Dropout(.3))
model.add(Bidirectional(GRU(units=146,activation='tanh')))
model.add(Dropout(.4))
model.add(Dense(73,activation='tanh'))
model.add(Dropout(.5))
model.add(Dense(4,activation="softmax"))
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

#path to save weights to: please change as needed
MODEL_DIR = Path(__file__).parent / "model"
checkpoint_path = MODEL_DIR / "model_weights.weights.h5"
#directory to save weights
checkpoint_dir = os.path.dirname(checkpoint_path)

#save weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,save_weights_only=True,verbose=1)

#early stopping: end training if loss does not improve after 5 epochs and restore the best weights
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss',patience=5,restore_best_weights=True)

#print model summary
print()
print(model.summary())

#train model, time training, and display time afterwards
train_start = time.time()
history = model.fit(X_train,y_train,epochs=50,batch_size=32,validation_data=(X_val, y_val),callbacks=[early_stopping,cp_callback],verbose=1)
train_end = time.time()-train_start
print()
print("Total time to train (in seconds):",train_end)
###############################################################################

#plot training loss versus validation loss
plt.plot(history.history['loss'], label='Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title("Training Loss")
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
plt.clf()

#plot training accuracy versus validation accuracy
plt.plot(history.history['accuracy'], label='Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title("Training Accuracy")
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
plt.clf()

print()
#test model, time testing, display time, and display accuracy
test_start = time.time()
results = model.evaluate(X_test, y_test, batch_size=32)
test_end = time.time()-test_start
print("Total time to test (in seconds):",test_end)
print()
print("Test accuracy:",results[1])


#plot a bar graph of the samples the model classified incorrectly according to game number
errors = [0,0,0,0]
#reiterate over test set and manually predict each point, and if incorrect, record
#the label of the error
for i in range(len(X_test)):   
    prediction = np.argmax(model.predict(np.array([X_test[i],]),verbose=0))
    ground_truth = np.argmax(y_test[i])
    if prediction!=ground_truth:
        errors[ground_truth]+=1 
game_errors = {"Game "+str(i+1):errors[i] for i in range(4)} #convert error list to dictionary
games = list(game_errors.keys())
values = list(game_errors.values())
#generate plot
fig = plt.figure(figsize = (10, 5))
plt.bar(games, values, color ='red', width = 0.4)
plt.xlabel("Games")
plt.ylabel("Number of errors")
plt.title("Number of errors made on test set by game")
plt.show()
###############################################################################