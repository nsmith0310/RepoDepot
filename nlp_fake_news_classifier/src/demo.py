#imports
import utility
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

kill_flag = False

#allow user to enter text and get predictions until they exit
while not kill_flag:
    print()
    document = input("Enter your sentence/document: ")
    print()
    print("Sentence/document S: "+document)
    print()
    preprocessed_data = utility.PREPROCESS([document])
    predictions = utility.TESTER(preprocessed_data, model, vocabulary, batch_size=1)
         
    label = "Fake news." if predictions[0][0]==1 else "Real news."
    print("was classified as "+label)
    
    print("P(Fake news | S) = "+str(predictions[0][2]))
    print("P(Real news | S) = "+str(predictions[0][1]))
    
    end = input("Do you want to enter another sentence [Y/N]? ")
    if end.lower()=="n" or end.lower()=="no":
        kill_flag=True