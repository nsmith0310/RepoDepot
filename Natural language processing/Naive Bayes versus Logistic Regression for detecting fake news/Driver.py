#main script

#imports
import sys
import Auxiliary


#get user arguments
args = sys.argv

#set arguments if either are out of predefined ranges
default_flag = False

if len(args)!=3:
    default_flag = True
try:
    ALGO = int(args[1])
    if ALGO < 0 or ALGO > 1:
        ALGO = 0
except:
    ALGO = 0
try:
    TRAIN_SIZE = int(args[2])
    if TRAIN_SIZE < 50 or TRAIN_SIZE > 80:
        TRAIN_SIZE = 80
except:
    TRAIN_SIZE = 80
    
if default_flag==True:
    ALGO = 0
    TRAIN_SIZE = 80
    
#get dataset
dataset = Auxiliary.GET_DATASET()

#preprocess dataset
preprocessed_data = Auxiliary.PREPROCESS([dataset[i][0] for i in range(len(dataset))])

#extract vocabulary
vocabulary = Auxiliary.GET_VOCABULARY(preprocessed_data)

#generate train-test split
train_test_data = [[preprocessed_data[i],dataset[i][1]] for i in range(len(dataset))]
X_train, X_test, y_train, y_test = Auxiliary.TRAIN_TEST_SPLIT(train_test_data,TRAIN_SIZE,len(dataset))

print("Training set size: "+str(TRAIN_SIZE)+" %")  

#select and train algorithm depending on user input
if ALGO==0:
    #train Naive Bayes model, test model, get metrics
    print("Classifier type: Naive Bayes")
    print()
    print("Training classifier…")
    model = Auxiliary.TRAINER(X_train,y_train,vocabulary,0,batch_size=128)
    print("Testing classifier…")   
    predictions = Auxiliary.TESTER(X_test, model, vocabulary,batch_size=128)    
    metrics = Auxiliary.EVALUATE(predictions, y_test)
    print()
else:
    #train Logistic Regression model, test model, get metrics
    print("Classifier type: Logistic Regression")
    print()
    print("Training classifier…")
    model = Auxiliary.TRAINER(X_train,y_train,vocabulary,1,batch_size=128)
    print("Testing classifier…")   
    predictions = Auxiliary.TESTER(X_test, model, vocabulary,batch_size=128,threshold=.5)
    metrics = Auxiliary.EVALUATE(predictions, y_test)
    print()
    
#display metrics
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

kill_flag = False

#allow user to enter text and get predictions until they exit
while not kill_flag:
    print()
    document = input("Enter your sentence/document: ")
    print()
    print("Sentence/document S: "+document)
    print()
    preprocessed_data = Auxiliary.PREPROCESS([document])
    predictions = Auxiliary.TESTER(preprocessed_data, model, vocabulary, batch_size=1)
         
    label = "Fake news." if predictions[0][0]==1 else "Real news."
    print("was classified as "+label)
    if ALGO==0:
        print("P(Fake news | S) = "+str(predictions[0][2]))
        print("P(Real news | S) = "+str(predictions[0][1]))
    print()
    end = input("Do you want to enter another sentence [Y/N]? ")
    if end.lower()=="n" or end.lower()=="no":
        kill_flag=True
    
        
    
    