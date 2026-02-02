#imports
import utility
import pickle
from pathlib import Path

#use train set size of 80 percent of the total dataset
TRAIN_SIZE = 80

#get the dataset using only the title column
dataset = utility.GET_DATASET(["title"])

#preprocess the dataset
preprocessed_data = utility.PREPROCESS([dataset[i][0] for i in range(len(dataset))],lowercase=False)

#extract vocabulary
vocabulary = utility.GET_VOCABULARY(preprocessed_data)

#train test split
traintest_data = [[preprocessed_data[i],dataset[i][1]] for i in range(len(dataset))]
X_train, X_test, y_train, y_test = utility.TRAIN_TEST_SPLIT(traintest_data,TRAIN_SIZE,len(dataset))

#train Naive Bayes
model = utility.TRAINER(X_train,y_train,vocabulary,0,batch_size=128)

#save all trained Naive Bayes parameters to .pkl files
MODEL_DIR = Path(__file__).parent / "model"

with open(MODEL_DIR / 'NB_model_positive_parameters.pkl', 'wb') as f:
    pickle.dump(model.positive_parameters, f)
with open(MODEL_DIR / 'NB_model_negative_parameters.pkl', 'wb') as f:
    pickle.dump(model.negative_parameters, f)
with open(MODEL_DIR / 'NB_model_positive_samples.pkl', 'wb') as f:
    pickle.dump(model.positive_samples, f)
with open(MODEL_DIR / 'NB_model_negative_samples.pkl', 'wb') as f:
    pickle.dump(model.negative_samples, f)
with open(MODEL_DIR / 'NB_model_vocabulary_size.pkl', 'wb') as f:
    pickle.dump(model.vocabulary_size, f)
with open(MODEL_DIR / 'vocabulary.pkl', 'wb') as f:
    pickle.dump(vocabulary, f)


    