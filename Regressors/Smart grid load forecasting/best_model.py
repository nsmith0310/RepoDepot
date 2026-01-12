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

#set aside june 2008 data
june2008_data = format_dataset(temps,loads,maps,summary='mean',features=add_features,june2008=True)
june2008_data = [zone[1] for zone in june2008_data]

#apply mapping
mappings = format_dataset(temps,loads,maps,summary='mean',features=add_features,preprocess=0)

#obtain train-validate-test split
partitions = train_val_test(mappings,val_percent,test_percent,mode=1)

X_train,X_validate,X_test,y_train,y_validate,y_test = partitions

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
#calculate scores on the training, validation, and test sets; time testing
train_score = score_gradient_boosting(models, X_train, y_train)
validation_score = score_gradient_boosting(models, X_validate, y_validate)
gb_testing_start_time = time.time()
test_score = score_gradient_boosting(models, X_test, y_test)
gb_testing_time = time.time()-gb_testing_start_time

#print out scores, and time
print("Gradient Boosting Regressor results:")
print("Training time: "+str(round(gb_training_time,precision))+" seconds")
print("Training average R^2: "+str(round(train_score[0],precision)))
print("Training average RPE: "+str(round(train_score[1],precision)))
print("Validation average R^2: "+str(round(validation_score[0],precision)))
print("Validation average RPE: "+str(round(validation_score[1],precision)))
print("Testing time: "+str(round(gb_testing_time,precision))+" seconds")
print("Testing average R^2: "+str(round(test_score[0],precision)))
print("Testing average RPE: "+str(round(test_score[1],precision)))
print()
print("Top prediction errors sorted in descending order by absolute RPE:")
print()
#print out top 10 errors
predictions = predict_gradient_boosting(models,X_test)
bad_predictions = worst_predictions(predictions,y_test, load_zone_metadata)
print(bad_predictions)
print()

#predict June 2008
june2008_predictions = predict_gradient_boosting(models,june2008_data)
#convert predictions to dataframe
june2008_dataframe = format_june2008(june2008_predictions, loads)
#save csv
save_csv(june2008_dataframe)
print("June 2008 predictions saved as 'Load_prediction.csv'")
