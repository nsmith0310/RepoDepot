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
#save non-hour columns to later recover
load_zone_metadata = backup(loads.to_numpy())

#apply mapping
mappings = format_dataset(temps,loads,maps,summary='mean',features=add_features,preprocess=0)

#obtain train-validate-test split
partitions = train_val_test(mappings,val_percent,test_percent,mode=1)

_ , _ , X_test, _ , _ , y_test = partitions

#Gradient Boosting

MODEL_DIR = Path(__file__).parent / "model"

with open(MODEL_DIR / 'KNN_model.pkl', 'rb') as f:
    models = pickle.load(f)

knn_testing_start_time = time.time()
test_score = score_knn(models, X_test, y_test)
knn_testing_time = time.time()-knn_testing_start_time

#print out scores, and time
print("KNN Regressor inference results:")
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


