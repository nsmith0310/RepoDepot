#demo script

#imports
import pickle
import NaiveBayesClassifier
import Auxiliary 
    
#load saved model parameters and vocabulary
LR_model = pickle.load(open('LR_model.pkl', 'rb'))
NB_model_negative_parameters = pickle.load(open('NB_model_negative_parameters.pkl', 'rb'))    
NB_model_positive_parameters = pickle.load(open('NB_model_positive_parameters.pkl', 'rb'))
NB_model_negative_samples = pickle.load(open('NB_model_negative_samples.pkl', 'rb'))    
NB_model_positive_samples = pickle.load(open('NB_model_positive_samples.pkl', 'rb'))
NB_model_vocabulary_size = pickle.load(open('NB_model_vocabulary_size.pkl', 'rb')) 
vocabulary = pickle.load(open('vocabulary.pkl', 'rb')) 

#set Naive Bayes parameters
NB_model = NaiveBayesClassifier.NaiveBayesModel(vocabulary)
NB_model.SET_PARAMETERS(NB_model_positive_parameters, 
                        NB_model_negative_parameters,
                        NB_model_positive_samples,
                        NB_model_negative_samples,
                        NB_model_vocabulary_size)

#real news headline
sample_text_1 = "Forecasts warn of possible winter storms across US during Thanksgiving week"
#fake news headline
sample_text_2 = "Former president Obama shocked the country when he announced he would be running for a third term."

demo_text = [sample_text_1,sample_text_2]

#preprocess
preprocessed_text = Auxiliary.PREPROCESS(demo_text,lowercase=False)

#get predictions
NB_predictions = Auxiliary.TESTER(preprocessed_text,NB_model,vocabulary,batch_size=3)
LR_predictions = Auxiliary.TESTER(preprocessed_text,LR_model,vocabulary,batch_size=3)


#display predictions
for index in range(len(demo_text)):
    NB_prediction = "fake" if NB_predictions[index][0]==1 else "real"
    NB_probs = [NB_predictions[index][1],NB_predictions[index][2]]
    LR_prediction = "fake" if LR_predictions[index][0]==1 else "real"
    LR_probs = [LR_predictions[index][1],LR_predictions[index][2]]
    print("Sample text "+str(index+1)+":")
    print(demo_text[index])
    print()
    print("Naive Bayes classified this text as "+NB_prediction+" news.")
    print("Naive Bayes probabilities: ")
    print("P(real news|sample"+str(index+1)+"):",NB_probs[0])
    print("P(fake news|sample"+str(index+1)+"):",NB_probs[1])
    print()
    print("Logistic Regression classified this text as "+LR_prediction+" news.")
    print("Logisitic Regression probabilities: ")
    print("P(real news|sample"+str(index+1)+"):",LR_probs[0])
    print("P(fake news|sample"+str(index+1)+"):",LR_probs[1])
    print()
    
#predict arbitary text sequence
sentence = input("Sentence:")
preprocessed_text = Auxiliary.PREPROCESS(demo_text,lowercase=False)
NB_predictions = Auxiliary.TESTER(preprocessed_text,NB_model,vocabulary,batch_size=1)
LR_predictions = Auxiliary.TESTER(preprocessed_text,LR_model,vocabulary,batch_size=1)

NB_prediction = "fake" if NB_predictions[0][0]==1 else "real"
NB_probs = [NB_predictions[0][1],NB_predictions[0][2]]
LR_prediction = "fake" if LR_predictions[0][0]==1 else "real"
LR_probs = [LR_predictions[0][1],LR_predictions[0][2]]

#display predictions
print()
print("Naive Bayes classified this text as "+NB_prediction+" news.")
print("Naive Bayes probabilities: ")
print("P(real news|sample):",NB_probs[0])
print("P(fake news|sample):",NB_probs[1])
print()
print("Logistic Regression classified this text as "+LR_prediction+" news.")
print("Logisitic Regression probabilities: ")
print("P(real news|sample):",LR_probs[0])
print("P(fake news|sample):",LR_probs[1])
print()