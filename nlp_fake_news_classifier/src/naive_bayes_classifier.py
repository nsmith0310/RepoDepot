#the core Naive Bayes class

#import
from math import log

#Naive Bayes model class
class NaiveBayesModel:
    
    #initialize model parameters 
    def __init__(self,vocabulary):
        self.vocabulary_size = len(vocabulary)
        self.positive_parameters = dict()
        self.negative_parameters = dict()
        for word in range(self.vocabulary_size):
            self.positive_parameters[word] = 0
            self.negative_parameters[word] = 0
        self.negative_samples = 0
        self.positive_samples = 0
        self.positive_vocabulary_size = 0
        self.negative_vocabulary_size = 0
    
    #used for loading saved models
    def SET_PARAMETERS(self,positive_parameters,negative_parameters,positive_samples,negative_samples,vocabulary_size):
        self.positive_parameters = positive_parameters
        self.negative_parameters = negative_parameters
        self.positive_samples = positive_samples
        self.negative_samples = negative_samples
        self.vocabulary_size = vocabulary_size
    
    #fit model
    def FIT(self,X,y):       
        
        #for each item in the training data
        #increment the count of the respective positive/negative examples seen
        #add the sum of the vector to the respective positive/negative total word count
        #add each item index to the parameter for that item
        #item indices represent the number of times a word appears in the document
        
        for index in range(len(X)):            
            if y[index]==0:
                self.negative_samples+=1
                self.negative_vocabulary_size+=sum(X[index])
                for sub_index in range(len(X[index])):                   
                    self.negative_parameters[sub_index]+=X[index][sub_index]                    
            else:             
                self.positive_samples+=1
                self.positive_vocabulary_size+=sum(X[index])
                for sub_index in range(len(X[index])):                   
                    self.positive_parameters[sub_index]+=X[index][sub_index]                   
    
    #this has to be computed separately with batch processing because we do not have 
    #complete counts until all batches have been processed in fit()
    #uses default smoothing parameter of 1
    def FINALIZE(self,smoothing=1):       
        #convert total sample counts to probabilities        
        self.negative_samples = self.negative_samples/(self.negative_samples+self.positive_samples)
        self.positive_samples = self.positive_samples/(self.negative_samples+self.positive_samples)
        #compute the final parameters by applying smoothing and normalizing
        for parameter in self.negative_parameters:
            self.negative_parameters[parameter] = self.negative_parameters[parameter] + smoothing
            self.negative_parameters[parameter] = self.negative_parameters[parameter]/(smoothing*self.vocabulary_size + self.negative_vocabulary_size)
        for parameter in self.positive_parameters:
            self.positive_parameters[parameter] = self.positive_parameters[parameter] + smoothing
            self.positive_parameters[parameter] = self.positive_parameters[parameter]/(smoothing*self.vocabulary_size + self.positive_vocabulary_size)
    
    #predict some set of documents using log-space
    def PREDICT(self,X,threshold=None):
        predictions = []
        log_negative_probability = log(self.negative_samples,10)
        log_positive_probability = log(self.positive_samples,10)
        for index in range(len(X)):
            negative_probability = log_negative_probability
            positive_probability = log_positive_probability
            for sub_index in range(len(X[index])):  
                    if X[index][sub_index]!=0:                          
                        negative_probability+=X[index][sub_index]*log(self.negative_parameters[sub_index],10)                                                                        
                        positive_probability+=X[index][sub_index]*log(self.positive_parameters[sub_index],10)
            #convert back from log space            
            negative_probability = 10**negative_probability
            positive_probability = 10**positive_probability
            
            #append predicted class and probabilities to list to return 
            if positive_probability>=negative_probability:
                predictions.append([1,negative_probability,positive_probability])
            else:
                predictions.append([0,negative_probability,positive_probability])
        return predictions 
            
        

