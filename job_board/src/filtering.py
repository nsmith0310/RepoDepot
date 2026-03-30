#imports
from transformers import pipeline
import re
import os

#load blacklisted titles into a list
BLACKLIST = os.path.join(os.path.dirname(__file__), "..", "text", "blacklist.txt")

blacklist = []
with open(BLACKLIST, 'r') as file:
    for line in file:
        text = line.strip()
        blacklist.append(text.lower())

#load classifier once at import time
_MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models", "ml_job_classifier_v2")
classifier = pipeline(
    "text-classification",
    model=_MODEL_DIR,
    tokenizer=_MODEL_DIR,
    device=0  # GPU
)

#apply first filter and discard jobs with titles in blacklist
def filter_one(jobs):
    positives = 0
    negatives = 0
    remainder = []
    for job in jobs:
        blacklisted = False
        for item in blacklist:
            if re.search(r"\b"+item+"\b", job["title"]):
                blacklisted = True
                break
        if blacklisted==False:
            remainder.append(job)
            positives+=1
        else:
            negatives+=1
    return remainder,positives,negatives

#apply second filter and discard jobs classified as negative by BERT
def filter_two(jobs):
    texts = ["Title: " + job["title"] + "\nDescription:\n" + job["description"] for job in jobs]
    results = classifier(texts, batch_size=16)

    labels = [int(r["label"].split("_")[1]) for r in results]
    remainder = [jobs[i] for i in range(len(jobs)) if labels[i]==1]
    positives = len(remainder)
    negatives = len(jobs)-positives
    return remainder,positives,negatives

#apply filtering, returning remaining jobs and logging information
def sift(jobs):
    passed_string_search,simple_positives,simple_negatives = filter_one(jobs)
    passed_bert,bert_positives,bert_negatives = filter_two(passed_string_search)
    return passed_bert,simple_positives,simple_negatives,bert_positives,bert_negatives
        
       