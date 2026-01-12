#import time
import time
#import models
from models import *
#import utilities
from utility import *
#import formatter
from formatter import *

#precision value
precision = 6
#load temperatures from csv
temps = pd.read_csv("../Temp_history_final.csv")
#load loads from csv
loads = pd.read_csv("../Load_history_final.csv")

#best mapping determined by mapping search
#top 3 stations per load zone as determined by KNN regression
maps = [[1, [1, 3, 7]],
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
#save non-hour columns to later recover
load_zone_metadata = backup(loads.to_numpy())

#apply mapping
mappings = format_dataset(temps,loads,maps,summary='mean',features=add_features,preprocess=0)

#obtain train-validate-test split
partitions = train_val_test(mappings,val_percent,test_percent,mode=1)

X_train,X_validate,X_test,y_train,y_validate,y_test = partitions

#KNN

#hyperparameter settings
n_neighbors = 5
weights = 'distance'
p = 1

#start timer
knn_training_start_time = time.time()
models = fit_knn(X_train,y_train,n_neighbors,weights,p,mode=1)
#stop timer

knn_training_time = time.time()-knn_training_start_time
#calculate scores on the training, validation, and test sets; time testing
train_score = score_knn(models, X_train, y_train)
validation_score = score_knn(models, X_validate, y_validate)
knn_testing_start_time = time.time()
test_score = score_knn(models, X_test, y_test)
knn_testing_time = time.time()-knn_testing_start_time

#print out scores, and time
print("KNN Regressor results:")
print()
print("Training time: "+str(round(knn_training_time,precision))+" seconds")
print("Training average R^2: "+str(round(train_score[0],precision)))
print("Training average RPE: "+str(round(train_score[1],precision)))
print("Validation average R^2: "+str(round(validation_score[0],precision)))
print("Validation average RPE: "+str(round(validation_score[1],precision)))
print("Testing time: "+str(round(knn_testing_time,precision))+" seconds")
print("Testing average R^2: "+str(round(test_score[0],precision)))
print("Testing average RPE: "+str(round(test_score[1],precision)))
print()
print("Top prediction errors sorted in descending order by absolute RPE:")
print()
#print out top 10 errors
predictions = predict_knn(models,X_test)
bad_predictions = worst_predictions(predictions,y_test, load_zone_metadata)
print(bad_predictions)
print()
