#import gradient boosting regressor
from sklearn.ensemble import GradientBoostingRegressor
#import knn regressor
from sklearn.neighbors import KNeighborsRegressor
#import numpy
import numpy as np  
#import utilities
from utility import *

# fit gradient boosting regressor and return one model for each hour column for each load zone
def fit_gradient_boosting(X_train,y_train,test_n_estimator,test_learning_rate,test_subsample,mode=1):
    #make a model for each load station
    all_models = []  
    #for each load zone
    for zone in range(len(X_train)):
        col_models = []
        #iterate over columns 
        for feature in range(len(y_train[zone])):
            #mode 1 allows use of hyperparameters
            if mode==1:             
                model = GradientBoostingRegressor(n_estimators=test_n_estimator,
                                                  learning_rate=test_learning_rate,                                                 
                                                  subsample=test_subsample,                                                 
                                                  random_state=0)         
            #mode 2 uses all default parameters except for random state
            else:
                model = GradientBoostingRegressor(random_state=0)
            #fit model for column
            model.fit(X_train[zone][feature],np.ravel(y_train[zone][feature]))
            #append column model
            col_models.append(model)
        #append all column models
        all_models.append(col_models)
    return all_models

#score gradient boosting; calculate both average r^2 over stations and average RPE
def score_gradient_boosting(models,X_test,y_test):  
    #r^2 score list
    r2_scores = []
    #target data which will be built iteratively
    target_data = None
    #predicted data which will be built iteratively
    predicted_data = None
    #for each load zone
    for zone in range(len(X_test)):
        #predictions for given load zone
        all_predictions = []
        #targets
        all_targets = []
        #iterate over columns
        for feature in range(len(y_test[zone])):
            #use trained model and make prediction              
            model = models[zone][feature]
            prediction = model.predict(X_test[zone][feature])
            #append prediction and target columns
            all_predictions.append(prediction)
            all_targets.append(y_test[zone][feature])
        #combine predictions and targets
        all_predictions = np.asanyarray(all_predictions).T
        all_targets = np.asanyarray(all_targets).T
        #append r^2 score for this load zone
        r2_scores.append(r2(all_targets[0], all_predictions))
        #add load zone targets
        if not isinstance(target_data,np.ndarray):
            target_data = all_targets[0]
        else:
            target_data = np.vstack((target_data,all_targets[0]))
        #add load zone predictions
        if not isinstance(predicted_data,np.ndarray):
            predicted_data = all_predictions
        else:
            predicted_data = np.vstack((predicted_data,all_predictions))
    #calculate average r^2
    avg_r2 = average_r2(r2_scores)
    #calculate average RPE
    avg_rpe = average_rpe(predicted_data, target_data)    
    return avg_r2, avg_rpe

#predict using models
def predict_gradient_boosting(models,X_test):  
    #iteratively build predicted data
    predicted_data = None
    #for each load zone
    for zone in range(len(X_test)):
        #predictions for given load zone
        all_predictions = []
        #targets
        all_targets = []
        #iterate over features
        for feature in range(len(X_test[zone])):
            #use trained model and make prediction              
            model = models[zone][feature]
            prediction = model.predict(X_test[zone][feature])
            #append prediction
            all_predictions.append(prediction)
        #combine predictions
        all_predictions = np.asanyarray(all_predictions).T
        #add load zone predictions
        if not isinstance(predicted_data,np.ndarray):
            predicted_data = all_predictions
        else:
            predicted_data = np.vstack((predicted_data,all_predictions))
    return predicted_data.astype(np.uint32)           

# fit KNN regressor and return one model for each hour column for each load zone
def fit_knn(X_train,y_train,test_n_neighbor,test_weight,test_p,mode=1): 
    #make a model for each load station
    all_models = []   
    #for each load zone
    for zone in range(len(X_train)):
        col_models = []
        #iterate over columns 
        for feature in range(len(y_train[zone])):
            #mode 1 allows use of hyperparameters
            if mode==1:
                model = KNeighborsRegressor(n_neighbors=test_n_neighbor,weights=test_weight,p=test_p)
            #mode 2 uses all default hyperparameters
            else:
                model = KNeighborsRegressor()
            #fit model for column
            model.fit(X_train[zone][feature],np.ravel(y_train[zone][feature]))
            #append column model
            col_models.append(model)
        #append all column models
        all_models.append(col_models)
    return all_models

#score KNN; calculate both average r^2 over stations and average RPE
def score_knn(models,X_test,y_test):  
    #r^2 score list
    r2_scores = []
    #target data which will be built iteratively
    target_data = None
    #predicted data which will be built iteratively
    predicted_data = None
    #for each load zone
    for zone in range(len(X_test)):
        #predictions for given load zone
        all_predictions = []
        #targets
        all_targets = []
        #iterate over columns
        for feature in range(len(y_test[zone])):
            #use trained model and make prediction              
            model = models[zone][feature]
            prediction = model.predict(X_test[zone][feature])
            #append prediction and target columns
            all_predictions.append(prediction)
            all_targets.append(y_test[zone][feature])
        #combine predictions and targets
        all_predictions = np.asanyarray(all_predictions).T
        all_targets = np.asanyarray(all_targets).T
        #append r^2 score for this load zone
        r2_scores.append(r2(all_targets[0], all_predictions))
        #add load zone targets
        if not isinstance(target_data,np.ndarray):
            target_data = all_targets[0]
        else:
            target_data = np.vstack((target_data,all_targets[0]))
        #add load zone predictions
        if not isinstance(predicted_data,np.ndarray):
            predicted_data = all_predictions
        else:
            predicted_data = np.vstack((predicted_data,all_predictions))
    #calculate average r^2
    avg_r2 = average_r2(r2_scores)
    #calculate average RPE
    avg_rpe = average_rpe(predicted_data, target_data)  
    return avg_r2, avg_rpe

#predict using models
def predict_knn(models,X_test):  
    #iteratively build predicted data
    predicted_data = None
    #for each load zone
    for zone in range(len(X_test)):
        #predictions for given load zone
        all_predictions = []
        #targets
        all_targets = []
        #iterate over features
        for feature in range(len(X_test[zone])):
            #use trained model and make prediction              
            model = models[zone][feature]
            prediction = model.predict(X_test[zone][feature])
            #append prediction
            all_predictions.append(prediction)
        #combine predictions
        all_predictions = np.asanyarray(all_predictions).T
        #add load zone predictions
        if not isinstance(predicted_data,np.ndarray):
            predicted_data = all_predictions
        else:
            predicted_data = np.vstack((predicted_data,all_predictions))
    return predicted_data.astype(np.uint32)             

