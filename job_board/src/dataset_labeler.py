#imports
from transformers import pipeline
import pandas as pd
import pickle
import os

#load model
classifier = pipeline(
    "text-classification",
    model=os.path.join(os.path.dirname(__file__), "..", "models", "ml_job_classifier_v1"),
    tokenizer=os.path.join(os.path.dirname(__file__), "..", "models", "ml_job_classifier_v1"),
    device=0  # GPU
)

#load unlabeled training data
TRAIN_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "unlabeled_train.pkl")
df = pd.read_pickle(TRAIN_PATH)

#get predictions, labels, and scores
df["text"] = "Title: " + df["title"] + "\nDescription:\n" + df["description"]
texts = df["text"].tolist()
results = classifier(texts, batch_size=16)
labels = [int(r["label"].split("_")[1]) for r in results]
scores = [r["score"] for r in results]

#label uncertain predictions
print()
print("############################ Beginning labeling ############################")
print()

new_samples = {"title":[],"description":[],"label":[]}

valid_labels = ["1","0"]

for i in range(len(scores)):
    if scores[i] <= .6:
        string = texts[i]
        print(string)
        while True:
            label = input("label:")
            if label in valid_labels:
                break
        row = df.iloc[i]
        new_samples["title"].append(row["title"])
        new_samples["description"].append(row["description"])
        new_samples["label"].append(label)
        print()

#combine newly labeled samples with original labeled dataset
old_samples = pd.read_pickle(os.path.join(os.path.dirname(__file__), "..", "data", "labeled_train.pkl"))
new_samples = pd.DataFrame(new_samples)
df_combined = pd.concat([old_samples, new_samples], axis=0, ignore_index=True)

#write new dataset
TRAIN_PATH_2 = os.path.join(os.path.dirname(__file__), "..", "data", "labeled_train_2.pkl")

with open(TRAIN_PATH_2, 'wb') as f:
    pickle.dump(df_combined, f)
    
print("Second trainset written.")


