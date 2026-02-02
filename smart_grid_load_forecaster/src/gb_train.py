#import time
import time
#import models
from models import *
#import utilities
from utility import *
#import formatter
from formatter import *
import os, pickle
from pathlib import Path

temps_path = os.path.join(os.path.dirname(__file__), "..", "data", "Temp_history_final.csv")
loads_path = os.path.join(os.path.dirname(__file__), "..", "data", "Load_history_final.csv")

#precision value
precision = 6
#load temperatures from csv
temps = pd.read_csv(temps_path)
#load loads from csv
loads = pd.read_csv(loads_path)

#best mapping determined by mapping search
#top 3 stations per load zone as determined by KNN regression
maps = \
[[1, [1, 3, 7]],
[2, [7, 6, 1]],
[3, [9, 8, 11]],
[4, [11, 9, 7]],
[5, [2, 10, 11]],
[6, [9, 8, 11]],
[7, [9, 11, 8]],
[8, [10, 2, 9]],
[9, [4, 8, 9]],
[10, [11, 9, 10]],
[11, [8, 4, 7]],
[12, [6, 7, 1]],
[13, [1, 3, 6]],
[14, [8, 4, 9]],
[15, [5, 3, 10]],
[16, [6, 7, 4]],
[17, [9, 11, 8]],
[18, [4, 6, 7]],
[19, [1, 2, 7]],
[20, [9, 11, 8]]]

#features to add
add_features = ['day_of_year','year','month','indexes','day_of_week']
#validation percent
val_percent = .1
#test percent
test_percent = .1

#apply mapping
mappings = format_dataset(temps,loads,maps,summary='mean',features=add_features,preprocess=0)

#obtain train-validate-test split
partitions = train_val_test(mappings,val_percent,test_percent,mode=1)

X_train, X_validate, _ , y_train, y_validate, _ = partitions

#Gradient Boosting

#hyperparameter settings
n_estimators = 125
learning_rate = .1
subsample = .8

#start timer
gb_training_start_time = time.time()
models = fit_gradient_boosting(X_train,y_train,n_estimators,learning_rate,subsample,mode=1)
#stop timer
gb_training_time = time.time()-gb_training_start_time
#calculate scores on the training and validation sets
train_score = score_gradient_boosting(models, X_train, y_train)
validation_score = score_gradient_boosting(models, X_validate, y_validate)

#save model to pickle file
MODEL_DIR = Path(__file__).parent / "model"

with open(MODEL_DIR / 'GB_model.pkl', 'wb') as f:
    pickle.dump(models, f)

#print out scores, and time
print("Gradient Boosting Regressor training results:")
print("Training time: "+str(round(gb_training_time,precision))+" seconds")
print("Training average R^2: "+str(round(train_score[0],precision)))
print("Training average RPE: "+str(round(train_score[1],precision)))
print("Validation average R^2: "+str(round(validation_score[0],precision)))
print("Validation average RPE: "+str(round(validation_score[1],precision)))
print("Gradient Boosting Regressor model saved.")


