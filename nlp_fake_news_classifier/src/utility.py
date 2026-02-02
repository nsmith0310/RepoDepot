#script to interface with model classes and apply other functions 

#imports
import random
import math
import logistic_regression_classifier
import naive_bayes_classifier
import pandas as pd
import os

random.seed(0)

#get the dataset from the two separate files; allows for feature selection
def GET_DATASET(include_features=["title","text","subject"]):
    #dataset paths
    true_news_path = os.path.join(os.path.dirname(__file__), "..", "data", "True.csv")
    fake_news_path = os.path.join(os.path.dirname(__file__), "..", "data", "Fake.csv")
    
    #determine which features, if any, to drop
    features_to_drop = [column for column in ["title","text","subject","date"] if column not in include_features]
    
    #samples after dropping features
    negative_samples = pd.read_csv(true_news_path).drop(features_to_drop,axis=1)
    positive_samples = pd.read_csv(fake_news_path).drop(features_to_drop,axis=1)
    
    #length of both sample sets
    negative_length = len(negative_samples)
    positive_length = len(positive_samples)
    
    #add labels to the dataframe
    negative_samples.insert(len(include_features),"label",[0 for i in range(len(negative_samples))],True)
    positive_samples.insert(len(include_features),"label",[1 for i in range(len(positive_samples))],True)
    
    positive_array = []
    negative_array = []
    
    #concatenate all features
    for index,row in positive_samples.iterrows():
        combined_text = []
        for i in range(len(include_features)):
            combined_text.append(row.iloc[i])
        positive_array.append([" ".join(combined_text),row["label"]])
        
    for index,row in negative_samples.iterrows():
        combined_text = []
        for i in range(len(include_features)):
            combined_text.append(row.iloc[i])
        negative_array.append([" ".join(combined_text),row["label"]])
    
    #interleave datasets
    difference_array = positive_array[negative_length:]
    positive_array = positive_array[:negative_length]
    
    dataset = []
    for i in range(negative_length):
        dataset.append(negative_array[i])
        dataset.append(positive_array[i])
    c = 0
    for i in range(len(difference_array)):
        dataset.insert(c,difference_array[i])
        c+=2
    
    return dataset 

#training function for batch training
#interfaces with both models
def TRAINER(X,y,vocabulary,ALGO,batch_size=32): 
    
    #split training data into batches
    X_batches = []
    y_batches = []
    
    for index in range(0,len(X)-batch_size+1,batch_size):
        X_batch = X[index:index+batch_size]
        y_batch = y[index:index+batch_size]
        X_batches.append(X_batch)
        y_batches.append(y_batch)
    
    if len(X)%batch_size!=0:
        x = len(X)-len(X)%batch_size
        X_batch = X[x:]
        y_batch = y[x:]
        X_batches.append(X_batch)
        y_batches.append(y_batch)
    
    #based on the selected algoirthm, initialize the appropriate model            
    if ALGO==0:
        model = naive_bayes_classifier.NaiveBayesModel(vocabulary)
    else:
        model = logistic_regression_classifier.LogisticRegressionModel()
    
    #vectorize the batch and pass it to the model
    for sample_index in range(len(X_batches)):
        vectorized = VECTORIZE(X_batches[sample_index],vocabulary)       
        model.FIT(vectorized,y_batches[sample_index])
    #needed for batch training Naive Bayes
    if ALGO==0:
        model.FINALIZE()
    return model

#testing function for batch testing
def TESTER(X,model,vocabulary,batch_size=32,threshold=.5):
    #split test data into batches
    X_batches = []
    for index in range(0,len(X)-batch_size+1,batch_size):
        X_batch = X[index:index+batch_size]
        X_batches.append(X_batch)      
    if len(X)%batch_size!=0:
        x = len(X)-len(X)%batch_size
        X_batch = X[x:]
        X_batches.append(X_batch)
    
    #vectorize each batch and pass to classifier
    #append prediction to list
    predictions = []
      
    for sample_index in range(len(X_batches)):
        vectorized = VECTORIZE(X_batches[sample_index],vocabulary)
        prediction = model.PREDICT(vectorized,threshold)
        for item in prediction:
            predictions.append(item)
    
    return predictions

#only includes option to lowercase; calls segment
def PREPROCESS(dataset,lowercase=False):  
    if lowercase==True:
        dataset = [dataset[i].lower() for i in range(len(dataset))]
        
    preprocessed_dataset = SEGMENT(dataset)  
    
    return preprocessed_dataset
    
#segment text by spaces
def SEGMENT(dataset):
    segmented_dataset = []
    
    for document in dataset:
        segmented_dataset.append(document.split())
        
    return segmented_dataset

#extract vocabulary from dataset
def GET_VOCABULARY(dataset):
    vocabulary = dict()
    index = 0
    
    for document in dataset:
        for word in document:
            
            if word not in vocabulary:
                vocabulary[word] = 1
            else:
                vocabulary[word] += 1
                    
    dictionary = [[vocabulary[x],x] for x in vocabulary]
    dictionary.sort(reverse=True)
    
    vocabulary = dict()
    counter = 0
    for i in range(len(dictionary)):
        vocabulary[dictionary[i][1]] = counter
        counter+=1
    
    return vocabulary 

#vectorize document using extracted vocabulary                    
def VECTORIZE(dataset,vocabulary):
    vectors = []
    for document in dataset:
        vector = [0 for i in range(len(vocabulary))]
        for word in document:
            if word in vocabulary:
                vector[vocabulary[word]]+=1

        vectors.append(vector)
    return vectors
 
#generate metrics for list of predictions and ground truths   
def EVALUATE(predictions,labels):   
        
    true_positives = 0
    false_positives = 0
    true_negatives = 0
    false_negatives = 0
    
    for item in range(len(predictions)):
        if predictions[item][0]==labels[item]:
            if predictions[item][0]==1:
                true_positives+=1
            else:
                true_negatives+=1
        else:
            if predictions[item][0]==1:
                false_positives+=1
            else:
                false_negatives+=1
    
    if true_positives+false_positives == 0:
        precision = 'NaN'
    else:
        precision = true_positives/(true_positives+false_positives)        
    if true_positives+false_negatives == 0:
        recall = 'NaN'
    else:
        recall = true_positives/(true_positives+false_negatives)        
    if true_negatives+false_positives == 0:
        specificity = 'NaN'
    else:
        specificity = true_negatives/(true_negatives+false_positives)       
    if true_negatives+false_negatives == 0:
        npv = 'NaN'
    else:
        npv = true_negatives/(true_negatives+false_negatives)    
    if true_positives+true_negatives+false_positives+false_negatives == 0:
        accuracy = 'NaN'
    else:
        accuracy = (true_positives+true_negatives)/(true_positives+true_negatives+false_positives+false_negatives)    
    if precision == 'NaN' or recall == 'NaN':
        f_score = 'NaN'
    elif precision == 0 and recall == 0:
        f_score = 'NaN'
    else:
        f_score = 2*precision*recall/(precision+recall)

    return [true_positives,true_negatives,false_positives,false_negatives,recall,specificity,precision,npv,accuracy,f_score]

#generate train-test split
def TRAIN_TEST_SPLIT(dataset,TRAIN_SIZE,dataset_length):
    test_index = dataset_length-round(dataset_length*.2)
    train_index = min(round(dataset_length*TRAIN_SIZE/100),test_index)    
    random.shuffle(dataset)
    X_train = [dataset[i][0] for i in range(train_index)]
    y_train = [dataset[i][1] for i in range(train_index)]
    X_test = [dataset[i][0] for i in range(test_index,dataset_length)]
    y_test = [dataset[i][1] for i in range(test_index,dataset_length)]
    
    return X_train, X_test, y_train, y_test


