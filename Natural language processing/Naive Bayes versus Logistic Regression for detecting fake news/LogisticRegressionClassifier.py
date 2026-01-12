#logistic regression classifier

#imports
from sklearn.linear_model import LogisticRegression

class LogisticRegressionModel:
    #initialize with warm_start=True
    def __init__(self):
        self.LR_model = LogisticRegression(warm_start=True)   
        
    #fit model - supports batch training as long as labels are not homogenous
    def FIT(self,X,y):
        self.LR_model.fit(X,y)
        
    #predict class with threshold
    def PREDICT(self,X,threshold=.5):
        probabilities = self.LR_model.predict_proba(X)
        predictions = []
        for prediction in probabilities:
            
            normalized_prediction = []
            normalized_prediction.append(prediction[0]/(prediction[0]+prediction[1]))
            normalized_prediction.append(prediction[1]/(prediction[0]+prediction[1]))
            
            if normalized_prediction[1]>=threshold:
                predictions.append([1]+normalized_prediction)
            else:
                predictions.append([0]+normalized_prediction)
    
        return predictions
                
        
