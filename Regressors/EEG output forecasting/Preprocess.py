#Created by Nicholas Smith, Christopher Hunter, Alex Rivera, Greg Ferdinand, Chih-Lun Kang

###############################################################################
#imports
import random
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler,MinMaxScaler

#allows for adding simple custom features 
#supports adding, subtracting, multiplying, or dividing two features
def SET_FEATURES(data_frame,selected_features):
    new_columns = pd.DataFrame()
    #for each feature represented as a string, split it by the operator
    #if applicable, perform the operation between the two columns, and add
    #the result to the new data frame; if no operation, just add the column
    for feature in selected_features:
        new_column = None
        if "/" in feature:
            features = feature.split("/")
            new_column = data_frame[features[0]]/data_frame[features[1]]
            new_columns.insert(0,feature,new_column,True)
        elif "*" in feature:
            features = feature.split("*")
            new_column = data_frame[features[0]]*data_frame[features[1]]
            new_columns.insert(0,feature,new_column,True)
        elif "+" in feature:
            features = feature.split("+")
            new_column = data_frame[features[0]]+data_frame[features[1]]
            new_columns.insert(0,feature,new_column,True)
        elif "-" in feature:
            features = feature.split("-")
            new_column = data_frame[features[0]]-data_frame[features[1]]
            new_columns.insert(0,feature,new_column,True)
        else: 
            new_column = data_frame[feature]
            new_columns.insert(0,feature,new_column,True)
    
    return new_columns

#scale data: 0 do nothing; 1 use z score scaling; 2 use min-max scaling
def SCALE(data_frame, scaling_mode=0):   
    if scaling_mode==0 or scaling_mode>2:
        scaled_data_frame = data_frame        
    elif scaling_mode==1:
       scaler = StandardScaler() 
       scaled_data_frame = scaler.fit_transform(data_frame)
    elif scaling_mode==2:
        scaler = MinMaxScaler()
        scaled_data_frame = scaler.fit_transform(data_frame)
    return scaled_data_frame
###############################################################################
#main preprocess function     
def PREPROCESS(k_timesteps,train_partition,dataset_proportion,scaling_mode,use_pca=False,pca_components=None,selected_features=None):   
    #total number of rows in dataset
    items = 4284224
     
    #enter the path of the dataset here, replacing the path in base_path
    #if you have the dataset from Kaggle, the path from this point on shouldnt need to be changed 
    #assumes windows filestructure
    base_path = "GAMEEMO\\"
    
    master_X, master_y, indices = [], [], []
    
    counter, index = 0, 0
    
    #traverse dataset directory structure
    for subject_number in range(1,29):
        if subject_number<10:
            subject = "(S0"+str(subject_number)+")"
        else:
            subject = "(S"+str(subject_number)+")"
        
        for game_number in range(1,5):
            genre = str(game_number)
            game_path_prefix = "\\Preprocessed EEG Data\\.csv format\\"
            game_path_suffix = "AllChannels.csv"
            game_path = game_path_prefix+subject[1:-1]+"G"+genre+game_path_suffix
            full_path = base_path+subject+game_path
            
            df = pd.read_csv(full_path)
            df.drop(df.columns[14], axis=1,inplace=True)
            
            #break dataset down into chunks of k_timesteps rows unless the total
            #number of sample rows exceeds the proportion specified
            if counter<dataset_proportion*items:
                for chunk in range(0,(len(df)//k_timesteps)*k_timesteps,k_timesteps):
                    data_frame = df.iloc[chunk:chunk+k_timesteps,:] #get k_timesteps from base data frame
                    data_frame = SET_FEATURES(data_frame, selected_features) #perform feature engineering
                    scaled_data_frame = SCALE(data_frame,scaling_mode) #scale features
                    #if using PCA, apply it
                    if use_pca==True:
                        reduced_data_frame = PCA(n_components=pca_components).fit_transform(scaled_data_frame)
                    else:
                        reduced_data_frame = scaled_data_frame
                    #append preprocessed data and corresponding label
                    master_X.append(reduced_data_frame)
                    master_y.append(game_number-1)
                    indices.append(index)
                    index+=1
                    counter+=k_timesteps
            else:
                break
    
    #shuffle data and partition it into train and test
    random.shuffle(indices)
    shuffled_X = [master_X[i] for i in indices]
    shuffled_y = [master_y[i] for i in indices]
       
    X_train,y_train,X_test,y_test = [],[],[],[]
    
    train_partition = round(train_partition*len(shuffled_X))
    test_partition = len(shuffled_X)-train_partition
    
    counter = 0
    while counter<train_partition:
        X_train.append(shuffled_X[counter])
        y_train.append(shuffled_y[counter])
        counter+=1
    while counter<len(shuffled_X):
        X_test.append(shuffled_X[counter])
        y_test.append(shuffled_y[counter])
        counter+=1
      
    return X_train,y_train,X_test,y_test
###############################################################################


    
        
        