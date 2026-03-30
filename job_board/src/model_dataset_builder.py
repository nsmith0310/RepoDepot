#imports
import pickle
import pandas as pd
import os

#load positives and negatives

POSITIVE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "positive_jobs.pkl")

with open(POSITIVE_PATH, 'rb') as f:
    positives = pickle.load(f)

NEGATIVE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "negative_jobs.pkl")

with open(NEGATIVE_PATH, 'rb') as f:
    negatives = pickle.load(f)
    
valid_labels = ["1","0"]

#dictionaries some of which will be saved

labeled_train = {"title":[],"description":[],"label":[]}

labeled_test = {"title":[],"description":[],"label":[]}

unlabeled_train = {"title":[],"description":[]}

positive_lengths = {positives[i][0]:len(positives[i][1]) for i in range(len(positives))}

positive_idxs = {positives[i][0]:0 for i in range(len(positives))}

negative_lengths = {negatives[i][0]:len(negatives[i][1]) for i in range(len(negatives))}

negative_idxs = {negatives[i][0]:0 for i in range(len(negatives))}

labeled_train_list = []

#loops evenly distribute positives and negatives

total = 0
while True:
    for i in range(len(positives)):
        if positive_idxs[positives[i][0]]<positive_lengths[positives[i][0]]:
            labeled_train_list.append(positives[i][1][positive_idxs[positives[i][0]]])
            positive_idxs[positives[i][0]]+=1
            total+=1
        if total==150:break
    if total==150:break
    
total = 0
while True:
    for i in range(len(negatives)):
        if negative_idxs[negatives[i][0]]<negative_lengths[negatives[i][0]]:
            labeled_train_list.append(negatives[i][1][negative_idxs[negatives[i][0]]])
            negative_idxs[negatives[i][0]]+=1
            total+=1
        if total==150:break
    if total==150:break
    
labeled_test_list = []

total = 0
while True:
    for i in range(len(positives)):
        if positive_idxs[positives[i][0]]<positive_lengths[positives[i][0]]:
            labeled_test_list.append(positives[i][1][positive_idxs[positives[i][0]]])
            positive_idxs[positives[i][0]]+=1
            total+=1
        if total==150:break
    if total==150:break
    
total = 0
while True:
    for i in range(len(negatives)):
        if negative_idxs[negatives[i][0]]<negative_lengths[negatives[i][0]]:
            labeled_test_list.append(negatives[i][1][negative_idxs[negatives[i][0]]])
            negative_idxs[negatives[i][0]]+=1
            total+=1
        if total==150:break
    if total==150:break
    

for i in range(len(positives)):
    for j in range(positive_idxs[positives[i][0]],positive_lengths[positives[i][0]]):    
        unlabeled_train["title"].append(positives[i][1][j]["title"])
        unlabeled_train["description"].append(positives[i][1][j]["description"][:500])

for i in range(len(negatives)):
    for j in range(negative_idxs[negatives[i][0]],negative_lengths[negatives[i][0]]):    
        unlabeled_train["title"].append(negatives[i][1][j]["title"])
        unlabeled_train["description"].append(negatives[i][1][j]["description"][:500])

unlabeled_train = pd.DataFrame(unlabeled_train)

print()
print("############################ Beginning labeling train positives ############################")
print()

#hand-label 300 jobs for train

counter = 0
for job in labeled_train_list:
    string = ""
    string += "Job title: \n"
    string += job["title"]+"\n"
    string += "Job description: \n"
    string += job["description"][:500]
    print(string)
    while True:
        label = input("label:")
        if label in valid_labels:
            break
    labeled_train["title"].append(job["title"])
    labeled_train["description"].append(job["description"][:500])
    labeled_train["label"].append(label)
    print()
    counter+=1
    if counter==150:
        print("############################ Beginning labeling train negatives ############################")
        print()

labeled_train = pd.DataFrame(labeled_train)

print()
print("############################ Beginning labeling test positives ############################")
print()

#hand-label 300 jobs for model evaluation

counter = 0
for job in labeled_test_list:
    string = ""
    string += "Job title: \n"
    string += job["title"]+"\n"
    string += "Job description: \n"
    string += job["description"][:500]
    print(string)
    while True:
        label = input("label:")
        if label in valid_labels:
            break
    labeled_test["title"].append(job["title"])
    labeled_test["description"].append(job["description"][:500])
    labeled_test["label"].append(label)
    print()
    counter+=1
    if counter==150:
        print("############################ Beginning labeling test negatives ############################")
        print()

#save all dataset partitions

labeled_test = pd.DataFrame(labeled_test)

LABELED_TRAIN_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "labeled_train.pkl")

with open(LABELED_TRAIN_PATH, 'wb') as f:
    pickle.dump(labeled_train, f)

UNLABELED_TRAIN_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "unlabeled_train.pkl")
    
with open(UNLABELED_TRAIN_PATH, 'wb') as f:
    pickle.dump(unlabeled_train, f)

LABELED_TEST_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "labeled_test.pkl")

with open(LABELED_TEST_PATH, 'wb') as f:
    pickle.dump(labeled_test, f)

print("All dataset partitions written.")