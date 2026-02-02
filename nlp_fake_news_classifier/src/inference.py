#imports
import utility
import matplotlib.pyplot as plt
import pickle
import naive_bayes_classifier
from pathlib import Path

MODEL_DIR = Path(__file__).parent / "model"

#load saved model parameters and vocabulary
NB_model_negative_parameters = pickle.load(open(MODEL_DIR / 'NB_model_negative_parameters.pkl', 'rb'))    
NB_model_positive_parameters = pickle.load(open(MODEL_DIR / 'NB_model_positive_parameters.pkl', 'rb'))
NB_model_negative_samples = pickle.load(open(MODEL_DIR / 'NB_model_negative_samples.pkl', 'rb'))    
NB_model_positive_samples = pickle.load(open(MODEL_DIR / 'NB_model_positive_samples.pkl', 'rb'))
NB_model_vocabulary_size = pickle.load(open(MODEL_DIR / 'NB_model_vocabulary_size.pkl', 'rb')) 
vocabulary = pickle.load(open(MODEL_DIR / 'vocabulary.pkl', 'rb')) 

#set Naive Bayes parameters
model = naive_bayes_classifier.NaiveBayesModel(vocabulary)
model.SET_PARAMETERS(NB_model_positive_parameters,
                     NB_model_negative_parameters,
                     NB_model_positive_samples,
                     NB_model_negative_samples,
                     NB_model_vocabulary_size)


#use train set size of 80 percent of the total dataset
TRAIN_SIZE = 80

#get the dataset using only the title column
dataset = utility.GET_DATASET(["title"])

#preprocess the dataset
preprocessed_data = utility.PREPROCESS([dataset[i][0] for i in range(len(dataset))],lowercase=False)

#train test split
traintest_data = [[preprocessed_data[i],dataset[i][1]] for i in range(len(dataset))]
X_train, X_test, y_train, y_test = utility.TRAIN_TEST_SPLIT(traintest_data,TRAIN_SIZE,len(dataset))

#test Naive Bayes
predictions = utility.TESTER(X_test, model, vocabulary, batch_size=128)

#initialize lists for making ROC curve
ROC_curve_NB = [[0],[0]]
ROC_curve_LR = [[0],[0]]
ROC_curve_LR_ext = [[],[]]

#compute metrics from testing
metrics = utility.EVALUATE(predictions, y_test)

#complete items needed for ROC curve
ROC_curve_NB[0].append(metrics[0]/(metrics[0]+metrics[3]))
ROC_curve_NB[1].append(metrics[2]/(metrics[2]+metrics[1]))
ROC_curve_NB[0].append(1)
ROC_curve_NB[1].append(1)

#print out metrics
print("Naive Bayes metrics using only titles")
print("Test results / metrics:")
print("Number of true positives: "+str(metrics[0]))
print("Number of true negatives: "+str(metrics[1]))
print("Number of false positives: "+str(metrics[2]))
print("Number of false negatives: "+str(metrics[3]))
print("Sensitivity (recall): "+str(metrics[4]))
print("Specificity: "+str(metrics[5]))
print("Precision: "+str(metrics[6]))
print("Negative predictive value: "+str(metrics[7]))
print("Accuracy: "+str(metrics[8]))
print("F-score: "+str(metrics[9]))      

#ROC curve
plt.plot(ROC_curve_NB[1],ROC_curve_NB[0])
plt.plot([0,1], [0,1], linestyle='dashed', color='black')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.title("ROC curve: Naive Bayes using only titles")
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.show()
plt.clf()