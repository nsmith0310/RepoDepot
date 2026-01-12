#import r^2 from sklearn
from sklearn.metrics import r2_score
#import train-test split from sklearn
from sklearn.model_selection import train_test_split
#import numpy
import numpy as np
#import pandas
import pandas as pd

#calculate r^2
def r2(targets,predictions):
    return r2_score(targets,predictions)

#calculate average r^2
def average_r2(scores):
    return sum(scores)/len(scores)

#calculate average RPE
def average_rpe(y_pred, y_true):
    #obtain absolute RPE values (otherwise averaging does not make sense)
    #due to positive and negative values
    rpe_vals = rpe(y_pred, y_true, abval=True)
    return np.mean(rpe_vals)

#imputation needed to to several 0 load values (which will cause RPE to fail)
def impute(array):
    #iterate over rows and columns and set 0 values to mean of row
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col]==0:
                array[row][col]=np.mean(array[row])
    return array

#calculate RPE
def rpe(y_pred, y_true, abval=False):
    #impute 0 values
    y_true=impute(y_true)
    #calculate RPE
    rpe_values = 100*(y_true-y_pred)/y_true
    #return absolute value if specified
    if abval==True:
        return np.abs(rpe_values)
    else:
        return rpe_values

#encoding function to make load values hashable
#works due to unique rows
def encode(vals):
    return '+'.join([str(x) for x in list(vals)])

#restore metadata to loads which have had it stripped during formatting
def restore(array,backup_dict):
    restored_array = None
    #iteratively restore original values
    for row in array:
        #get metadata from backup dictionary by using encoded load values
        data = backup_dict[encode(row)]
        #restore original row
        complete_data = np.concatenate((data,row))
        #concatenate original row to array
        if not isinstance(restored_array,np.ndarray):
            restored_array = complete_data
        else:
            restored_array = np.vstack((restored_array,complete_data))
    return restored_array

#save load zone metadata
def backup(array):
    hashed_metadata = dict()
    #go over array and hash metadata using encoded load values
    for row in array:
        data,vals = row[:4],row[4:]
        string = encode(vals)
        hashed_metadata[string]=data
    return hashed_metadata
        
#calculate top ten worst predictions
def worst_predictions(predictions,y_test, load_zone_metadata):
    #create y test from separated columns
    y_test = np.concatenate([np.concatenate(x,axis=1) for x in y_test],axis=0)
    #calculate RPE and absolute RPE (latter of which is used for sorting)
    calculate_rpe,calculate_abs_rpe = rpe(predictions,y_test),rpe(predictions,y_test, abval=True)
    #restore y test metadata
    restored_y_test = restore(y_test,load_zone_metadata)
    #convert RPEs to vertical columns and join on axis 1
    rpe_vertical_format = np.asarray([calculate_rpe.flatten()]).T
    abs_rpe_vertical_format = np.asarray([calculate_abs_rpe.flatten()]).T
    rpes = np.concatenate((rpe_vertical_format,abs_rpe_vertical_format),axis=1)
    hours, metadata = [],[]
    #iterate over each value and obtain hour corresponding to it
    counter = 1
    for idx in range(len(rpe_vertical_format)):
        hours.append(counter)
        counter+=1
        if counter==25:
            counter = 1
    #iterate over restored y test and append metadata
    for idx in range(len(restored_y_test)):
        for hour in range(24):
            metadata.append(restored_y_test[idx][:4])
    #convert hours, metadata, predictions, and targets to vertical columns and join
    hours,metadata = np.asarray([hours]).T,np.asarray(metadata)
    metadata = np.hstack((metadata,hours),dtype=object)
    vert_prediction,vert_true = np.asarray([predictions.flatten()]).T,np.asarray([y_test.flatten()]).T
    loads = np.hstack((vert_prediction,vert_true),dtype=object)
    metadata = np.hstack((metadata,loads),dtype=object)
    vertical_format=np.hstack((metadata,rpes),dtype=object)
    #sort combined array by absolute RPE
    vertical_format = vertical_format[vertical_format[:, -1].argsort()][::-1]
    #drop absolute RPE
    vertical_format = np.delete(vertical_format, -1, axis=1)[:10]
    #convert to dataframe and add column names for display
    vertical_format = pd.DataFrame(vertical_format)
    vertical_format.columns = ['Zone','Year','Month','Day','Hour','Predicted load','True load','RPE']
    return vertical_format

#make train-validation-test split or just train-test split
def train_val_test(mappings,val_percent,test_percent,mode=1):   
    #train-validate-test split
    if mode==1:
        list_of_partitions = [[[] for model in range(20)] for part in range(6)]
    #train-test split
    else:
        list_of_partitions = [[[] for model in range(20)] for part in range(4)]
    #recalculte test percent if using a validation partition
    if mode==1:
        test_percent = test_percent/(1-val_percent)
    #iterate over each load zone and each column and use sklearn to apply split
    for mapping in range(len(mappings)):           
        for col in range(len(mappings[mapping][0])):
            #train-validate-test split
            if mode==1:
                X_train, X_validate, y_train, y_validate = train_test_split(mappings[mapping][1][col], 
                                                                            mappings[mapping][0][col], 
                                                                            test_size=val_percent, 
                                                                            random_state=0)  
                X_train, X_test, y_train, y_test = train_test_split(X_train, 
                                                                    y_train, 
                                                                    test_size=test_percent, 
                                                                    random_state=0)
                list_of_partitions[0][mapping].append(X_train)
                list_of_partitions[1][mapping].append(X_validate)
                list_of_partitions[2][mapping].append(X_test)
                list_of_partitions[3][mapping].append(y_train)
                list_of_partitions[4][mapping].append(y_validate)
                list_of_partitions[5][mapping].append(y_test)
            #train-test split
            else:
                X_train, X_test, y_train, y_test = train_test_split(mappings[mapping][1][col], 
                                                                    mappings[mapping][0][col], 
                                                                    test_size=test_percent, 
                                                                    random_state=0)
                list_of_partitions[0][mapping].append(X_train)
                list_of_partitions[1][mapping].append(X_test)
                list_of_partitions[2][mapping].append(y_train)
                list_of_partitions[3][mapping].append(y_test)               
    return list_of_partitions