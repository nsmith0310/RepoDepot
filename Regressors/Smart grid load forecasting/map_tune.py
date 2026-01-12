#import pandas
import pandas as pd
#import numpy
import numpy as np
#import models
from models import *
#import utilities
from utility import *
#import formatter
from formatter import *
#import time
import time

#precision for display
precision=6

#time mapping search
mapping_start_time = time.time()

#load temperatures from csv
temperatures = pd.read_csv("../Temp_history_final.csv")
#load loads from csv
loads = pd.read_csv("../Load_history_final.csv")

#initialize list of "monomaps" which will just consist of all mappings between
#one load zone and one temperature station
all_monomaps = []

#iterate over each load zone and temperature station pair and make pairs in
#format suitable for formatter
for temperature_station in range(1,12):
    temperature_monomaps = []
    for load_zone in range(1,21):
        temperature_monomaps.append([load_zone,[temperature_station]])
    all_monomaps.append(temperature_monomaps)
    
#formatter parameters
#features to add
add_features = ['day_of_year','year','month','indexes','day_of_week']
#train percentage to use when finding the mapping
mapping_train_percent = .8
#validation percentage to use when finding the mapping
mapping_validation_percent = .1

zone_monomaps = [[] for idx in range(20)]

#for each one-one mapping, format the dataset such that one temperature station
#is mapped to one load zone; splits into separate columns,
#and adds day of the year as a feature 
for monomapping in all_monomaps:     
    mappings = format_dataset(temperatures,loads,monomapping,summary='mean',features=add_features,preprocess=0)
    for idx in range(len(mappings)):
        zone_monomaps[idx].append(mappings[idx])
            
#import different algorithms to make different mappings
#import KNN regressor
from sklearn.neighbors import KNeighborsRegressor
#import decision tree regressor
from sklearn.tree import DecisionTreeRegressor
#import linear regression to use with polynomial features 
from sklearn.linear_model import LinearRegression
#import PolynomialFeatures for quadratic and cubic regression
from sklearn.preprocessing import PolynomialFeatures
#import r2 as this needs to be done manually when columns are split
from sklearn.metrics import r2_score

#initialize maps list to contain the station scores 
maps = [[],[],[],[]]

#iterate over formatted datasets
for zone in range(len(zone_monomaps)):
    #contains all one-one mappings for a single load zone
    possible_mappings = zone_monomaps[zone]
    #train percent converted to index
    train_percent = int(len(possible_mappings[0][0][0])*mapping_train_percent)
    #validation percent converted to index
    val_percent = int(len(possible_mappings[0][0][0])*mapping_validation_percent) + train_percent
    #decision tree station scores list
    dtr_station_scores = []
    #knn regression station scores list
    knn_station_scores = []
    #quadratic regression station scores list
    poly2_station_scores = []
    #cubic regression station scores list
    poly3_station_scores = []  
    #iterate over each station
    for station in range(11):
        #set features and targets
        X,Y = possible_mappings[station][1],possible_mappings[station][0]
        #set training and testing sets    
        X_train = [x[:train_percent] for x in X]
        X_validate = [x[train_percent:val_percent] for x in X]
        y_train = [y[:train_percent] for y in Y]
        y_validate = [y[train_percent:val_percent] for y in Y]
        #all individual algorithm predictions needed due to split columns
        dtr_predictions,knn_predictions,poly2_predictions,poly3_predictions = [],[],[],[]
        #iterate over each hour and create a separate model for that hour
        #do for each algorithm
        for feature in range(len(y_train)):
            #decision treee model                 
            dtr_model = DecisionTreeRegressor(random_state=0)           
            dtr_model.fit(X_train[feature],np.ravel(y_train[feature]))
            dtr_prediction = dtr_model.predict(X_validate[feature])
            dtr_predictions.append(dtr_prediction)
            #knn model
            knn_model = KNeighborsRegressor()           
            knn_model.fit(X_train[feature],np.ravel(y_train[feature]))
            knn_prediction = knn_model.predict(X_validate[feature])
            knn_predictions.append(knn_prediction)
            #quadratic regression model
            quad = PolynomialFeatures(degree=2, include_bias=False)
            quad_features = quad.fit_transform(X_train[feature])
            poly2_model = LinearRegression()           
            poly2_model.fit(quad_features,np.ravel(y_train[feature]))
            quad_test_features = quad.fit_transform(X_validate[feature])
            poly2_prediction = poly2_model.predict(quad_test_features)
            poly2_predictions.append(poly2_prediction)
            #cubic regression model
            cubic = PolynomialFeatures(degree=3, include_bias=False)
            cubic_features = cubic.fit_transform(X_train[feature])
            poly3_model = LinearRegression()           
            poly3_model.fit(cubic_features,np.ravel(y_train[feature]))
            cubic_test_features = cubic.fit_transform(X_validate[feature])
            poly3_prediction = poly3_model.predict(cubic_test_features)
            poly3_predictions.append(poly3_prediction)            
        #combine decision tree hour predictions into one day                    
        dtr_predictions = np.asanyarray(dtr_predictions).T              
        #combine knn hour predictions into one day                    
        knn_predictions = np.asanyarray(knn_predictions).T             
        #combine quadratic regression hour predictions into one day                    
        poly2_predictions = np.asanyarray(poly2_predictions).T                
        #combine cubic regression hour predictions into one day                    
        poly3_predictions = np.asanyarray(poly3_predictions).T  
        #combine hour targets into one day
        y_validate = np.concatenate(y_validate, axis=1)          
        #score the decision tree predictions for the day; append to scores      
        dtr_r2 = r2_score(y_validate, dtr_predictions)
        dtr_station_scores.append([dtr_r2,station+1])
        #score the knn predictions for the day; append to scores      
        knn_r2 = r2_score(y_validate, knn_predictions)
        knn_station_scores.append([knn_r2,station+1])
        #score the quadratic predictions for the day; append to scores      
        poly2_r2 = r2_score(y_validate, poly2_predictions)
        poly2_station_scores.append([poly2_r2,station+1])
        #score the cubic predictions for the day; append to scores      
        poly3_r2 = r2_score(y_validate, poly3_predictions)
        poly3_station_scores.append([poly3_r2,station+1])       
    #sort decision tree stations by r^2 in descending order; save scores
    dtr_station_scores.sort(key=lambda x: x[0], reverse=True)
    maps[0].append(dtr_station_scores)
    #sort knn stations by r^2 in descending order; save scores
    knn_station_scores.sort(key=lambda x: x[0], reverse=True)
    maps[1].append(knn_station_scores)
    #sort quadratic stations by r^2 in descending order; save scores
    poly2_station_scores.sort(key=lambda x: x[0], reverse=True)
    maps[2].append(poly2_station_scores)
    #sort cubic stations by r^2 in descending order; save scores
    poly3_station_scores.sort(key=lambda x: x[0], reverse=True)
    maps[3].append(poly3_station_scores)

#map list for each algorithm
map_list = [[],[],[],[]]

for algorithm in range(4):
    #iterate over each station score list and make final mappings up to each index
    #this has the effect of making a mapping (for each load zone) between a load
    #zone and its k best stations, k+1 best stations etc
    for idx in range(1,12):
        for zone in range(20):
            zone_map = [zone+1]
            zone_map.append([i[1] for i in maps[algorithm][zone][:idx]])
            map_list[algorithm].append(zone_map)

#obtain named maps
knn_maps,dtr_maps,poly2_maps,poly3_maps = map_list
#validation and test percents
val_percent,test_percent = .1,.1
#determine best mapping; set best algorithm, mapping length, and score
best_mapping_algorithm,best_length,best_score = None,None,-float('inf')

#iterate over temperature stations
for idx in range(1,12):
    #initialize mappings for each algorithm up to each index
    knn = [x for x in knn_maps if len(x[1])==idx]
    dtr = [x for x in dtr_maps if len(x[1])==idx]
    poly2 = [x for x in poly2_maps if len(x[1])==idx]
    poly3 = [x for x in poly3_maps if len(x[1])==idx]
    #format dataset using knn mapping, and obtain train-validation-test split
    mappings = format_dataset(temperatures,loads,knn,summary='mean',features=add_features,preprocess=0)
    partitions = train_val_test(mappings,val_percent,test_percent,mode=1)
    X_train,X_validate,X_test,y_train,y_validate,y_test = partitions
    #fit and score gradient boosting on given knn mapped dataset
    models = fit_gradient_boosting(X_train, y_train,None,None,None,mode=2)
    knn_score = score_gradient_boosting(models,X_validate,y_validate)
    #if score is best, save algorithm, mapping length, and score
    if knn_score[0]>best_score:
        best_score,best_mapping_algorithm,best_length = knn_score[0],0,idx
    #format dataset using decision tree mapping, and obtain train-validation-test split
    mappings = format_dataset(temperatures,loads,dtr,summary='mean',features=add_features,preprocess=0)
    partitions = train_val_test(mappings,val_percent,test_percent,mode=1)
    X_train,X_validate,X_test,y_train,y_validate,y_test = partitions
    #fit and score gradient boosting on given decision tree mapped dataset
    models = fit_gradient_boosting(X_train, y_train,None,None,None,mode=2)
    dtr_score = score_gradient_boosting(models,X_validate,y_validate)
    #if score is best, save algorithm, mapping length, and score
    if dtr_score[0]>best_score:
        best_score,best_mapping_algorithm,best_length = dtr_score[0],1,idx
    #format dataset using quadratic regression mapping, and obtain train-validation-test split    
    mappings = format_dataset(temperatures,loads,poly2,summary='mean',features=add_features,preprocess=0)
    partitions = train_val_test(mappings,val_percent,test_percent,mode=1)
    X_train,X_validate,X_test,y_train,y_validate,y_test = partitions
    #fit and score gradient boosting on given quadratic regression mapped dataset
    models = fit_gradient_boosting(X_train, y_train,None,None,None,mode=2)
    poly2_score = score_gradient_boosting(models,X_validate,y_validate)
    #if score is best, save algorithm, mapping length, and score
    if poly2_score[0]>best_score:
        best_score,best_mapping_algorithm,best_length = poly2_score[0],2,idx
    #format dataset using cubic regression mapping, and obtain train-validation-test split
    mappings = format_dataset(temperatures,loads,poly3,summary='mean',features=add_features,preprocess=0)
    partitions = train_val_test(mappings,val_percent,test_percent,mode=1)
    X_train,X_validate,X_test,y_train,y_validate,y_test = partitions
    #fit and score gradient boosting on given cubic regression mapped dataset
    models = fit_gradient_boosting(X_train, y_train,None,None,None,mode=2)
    poly3_score = score_gradient_boosting(models,X_validate,y_validate)
    #if score is best, save algorithm, mapping length, and score
    if poly3_score[0]>best_score:
        best_score,best_mapping_algorithm,best_length = poly3_score[0],3,idx

#end mapping search timer
mapping_time = time.time()-mapping_start_time
#print out best mapping, best mapping r^2, time taken to find mapping, and the mapping itself
best_mapping = []
if best_mapping_algorithm==0:
    print("Best mapping algorithm: KNN regressor")   
    best_mapping = [x for x in knn_maps if len(x[1])==best_length]
elif best_mapping_algorithm==1:
    print("Best mapping algorithm: Decision Tree regressor")
    best_mapping = [x for x in dtr_maps if len(x[1])==best_length]
elif best_mapping_algorithm==2:
    print("Best mapping algorithm: Quadratic Regression")
    best_mapping = [x for x in poly2_maps if len(x[1])==best_length]
elif best_mapping_algorithm==3:
    print("Best mapping algorithm: Cubic Regression")
    best_mapping = [x for x in poly3_maps if len(x[1])==best_length]
print("Best mapping length: "+str(best_length))
print("Highest average R^2 obtained by Gradient Boosting on best mapping: "+str(round(best_score,precision)))    
print("Time taken to search: "+str(round(mapping_time,precision))+" seconds")
print()
print("Mappings:")
print("Format: [Load zone, [Temperature stations]]")
for mapping in best_mapping:
    print(mapping)
print()

#validation percent and test percent for hyperparameter tuning
val_percent,test_percent = .1,.1

#apply mapping
mappings = format_dataset(temperatures,loads,best_mapping,summary='mean',features=add_features,preprocess=0)

#obtain train-validate-test split
partitions = train_val_test(mappings,val_percent,test_percent,mode=1)

X_train,X_validate,X_test,y_train,y_validate,y_test = partitions

#KNN

#hyperparameters to test
test_n_neighbors = [1,2,5,10,25,50]
test_weights = ['distance','uniform']
test_ps = [1,1.5,2,2.5]

#best hyperparameters
best_n_neighbors = None
best_weights = None
best_p = None

#best validation score
best_validation_score = -float('inf')
#best validation average rpe
best_validation_rpe = None
#best training score
best_training_score = None
#best training average rpe
best_train_rpe = None

#start timer
knn_tuning_start_time = time.time()

#iterate over each n_neigbors test value
for test_n_neighbor in test_n_neighbors:
    #iterate over each weights test value
    for test_weight in test_weights:
        #iterate over each p test value
        for test_p in test_ps:
            #train knn using test hyperparameters
            models = fit_knn(X_train,y_train,test_n_neighbor,test_weight,test_p,mode=1)
            #obtain score on training and validation sets
            score = score_knn(models, X_validate, y_validate)
            train_score = score_knn(models, X_train, y_train)
            #if score is the best seen, save all test hyperparameters and scores
            if score[0]>best_validation_score:
                best_validation_score=score[0]
                best_validation_rpe = score[1]
                best_training_score,best_train_rpe = train_score
                best_n_neighbors = test_n_neighbor
                best_weights = test_weight
                best_p = test_p
                
#stop timer
knn_tuning_time = time.time()-knn_tuning_start_time

#print out best scores, time, and hyperparameter values
print("KNN Regressor hyperparameter tuning results:")
print("Grid search runtime: "+str(round(knn_tuning_time,precision))+" seconds")
print("Best training average R^2: "+str(round(best_training_score,precision)))
print("Best training average RPE: "+str(round(best_train_rpe,precision)))
print("Best validation average R^2: "+str(round(best_validation_score,precision)))
print("Best validation average RPE: "+str(round(best_validation_rpe,precision)))
print("Best 'n_neighbors' value: "+str(best_n_neighbors))
print("Best 'weights' value: "+str(best_weights))
print("Best 'p' value: "+str(best_p))
print()

###############################################################################

#Gradient Boosting

#hyperparameters to test
test_n_estimators = [50,75,100,125]
test_learning_rates = [.01,.05,.1,.25,.5]
test_subsamples = [.5,.7,.8,.9,1.0]

#best hyperparameters
best_n_estimators = None
best_learning_rate = None
best_subsample = None

#best validation score
best_validation_score = -float('inf')
#best validation average rpe
best_validation_rpe = None
#best training score
best_training_score = None
#best training average rpe
best_train_rpe = None

#start timer
gb_tuning_start_time = time.time()

#iterate over each n_estimators test value
for test_n_estimator in test_n_estimators:
    #iterate over each learning_rate test value
    for test_learning_rate in test_learning_rates:
        #iterate over each subsample test value
        for test_subsample in test_subsamples:
            #train gradient boosting using test hyperparameters
            models = fit_gradient_boosting(X_train,y_train,test_n_estimator,test_learning_rate,test_subsample,mode=1)
            #obtain score on training and validation sets
            score = score_gradient_boosting(models, X_validate, y_validate)
            train_score = score_gradient_boosting(models, X_train, y_train)
            #if score is the best seen, save all test hyperparameters and scores
            if score[0]>best_validation_score:
                best_validation_score=score[0]
                best_validation_rpe = score[1]
                best_training_score,best_train_rpe = train_score
                best_n_estimators = test_n_estimator
                best_learning_rate = test_learning_rate
                best_subsample = test_subsample
                
#stop timer
gb_tuning_time = time.time()-knn_tuning_start_time

#print out best scores, time, and hyperparameter values
print("Gradient Boosting Regressor hyperparameter tuning results:")
print("Grid search runtime: "+str(round(gb_tuning_time,precision))+" seconds")
print("Best training average R^2: "+str(round(best_training_score,precision)))
print("Best training average RPE: "+str(round(best_train_rpe,precision)))
print("Best validation average R^2: "+str(round(best_validation_score,precision)))
print("Best validation average RPE: "+str(round(best_validation_rpe,precision)))
print("Best 'n_estimators' value: "+str(best_n_estimators))
print("Best 'learning_rate' value: "+str(best_learning_rate))
print("Best 'subsample' value: "+str(best_subsample))
print()
