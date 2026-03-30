#imports
import pandas as pd
import numpy as np
import torch
from datasets import Dataset, concatenate_datasets
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import os
import json

#dataset paths
MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "models", "ml_job_classifier_v2")
IRRELEVANT_FILE = os.path.join(os.path.dirname(__file__), "..", "text", "irrelevant_jobs.jsonl")
RELEVANT_FILE = os.path.join(os.path.dirname(__file__), "..", "text", "relevant_jobs.jsonl")
BASE_DATASET = os.path.join(os.path.dirname(__file__), "..", "data", "labeled_train_2.pkl")

#load original dataset
df_orig = pd.read_pickle(BASE_DATASET)
df_orig["label"] = df_orig["label"].astype(int)
df_orig["text"] = "Title: " + df_orig["title"] + "\nDescription:\n" + df_orig["description"]

#load user feedback dataset
feedback_examples = []

if os.path.exists(IRRELEVANT_FILE):
    with open(IRRELEVANT_FILE, "r") as f:
        for line in f:
            job = json.loads(line)
            text = f"Title: {job['title']}\nDescription:\n{job['description']}"
            feedback_examples.append({"text": text, "label": 0})

if os.path.exists(RELEVANT_FILE):
    with open(RELEVANT_FILE, "r") as f:
        for line in f:
            job = json.loads(line)
            text = f"Title: {job['title']}\nDescription:\n{job['description']}"
            feedback_examples.append({"text": text, "label": 1})

df_feedback = pd.DataFrame(feedback_examples).sample(frac=1, random_state=42)

#create train/validation split
train_orig, val_orig = train_test_split(df_orig, test_size=0.2, stratify=df_orig["label"], random_state=42)

#dynamic oversample factor
target_ratio = 0.05  
n_base = len(train_orig)
n_feedback = len(df_feedback)

oversample_factor = max(1, int(n_base / max(n_feedback, 1) * target_ratio))

#oversample feedback
df_feedback_oversampled = pd.concat([df_feedback]*oversample_factor, ignore_index=True)
df_feedback_oversampled = df_feedback_oversampled.sample(frac=1, random_state=42)

#combine with base training set
train_df = pd.concat([train_orig, df_feedback_oversampled]).sample(frac=1, random_state=42)
val_df = val_orig

#convert to hf datasets
train_dataset = Dataset.from_pandas(train_df, preserve_index=False)
val_dataset = Dataset.from_pandas(val_df, preserve_index=False)

#load tokenizer and format datasets
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR, trust_remote_code=True)

def tokenize(batch):
    return tokenizer(batch["text"], truncation=True, padding="max_length", max_length=512)

train_dataset = train_dataset.map(tokenize, batched=True)
val_dataset = val_dataset.map(tokenize, batched=True)
train_dataset.set_format("torch", columns=["input_ids", "attention_mask", "label"])
val_dataset.set_format("torch", columns=["input_ids", "attention_mask", "label"])

#load model
model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR, num_labels=2, trust_remote_code=True)

#define metrics
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average="binary")
    acc = accuracy_score(labels, preds)
    return {"accuracy": acc, "precision": precision, "recall": recall, "f1": f1}

#training arguments
training_args = TrainingArguments(
    output_dir=MODEL_DIR,
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    learning_rate=2e-6,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=8,
    num_train_epochs=2,
    weight_decay=0.01,
    load_best_model_at_end=True,
    metric_for_best_model="f1",
    greater_is_better=True,
    save_total_limit=1,
    fp16=torch.cuda.is_available(),
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    compute_metrics=compute_metrics,
)

#train and save
trainer.train()
trainer.save_model(MODEL_DIR)
tokenizer.save_pretrained(MODEL_DIR)
print("Model updated in-place at:", MODEL_DIR)