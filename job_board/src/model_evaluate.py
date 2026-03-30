#imports
import pandas as pd
import numpy as np
import torch
from datasets import Dataset
import os

#model pipeline
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments
)

from sklearn.metrics import accuracy_score, precision_recall_fscore_support

#load test dataset

LABELED_TEST_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "labeled_test.pkl")

df = pd.read_pickle(LABELED_TEST_PATH)

df["label"] = df["label"].astype(int)

df["text"] = "Title: " + df["title"] + "\nDescription:\n" + df["description"]

test_set = Dataset.from_pandas(
    df[["text", "label"]],
    preserve_index=False
)

#load tokenizer and format dataset

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "ml_job_classifier_v2")

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

def tokenize(batch):
    return tokenizer(
        batch["text"],
        truncation=True,
        padding="max_length",
        max_length=512
    )

test_set = test_set.map(tokenize, batched=True)

test_set.set_format(
    "torch",
    columns=["input_ids", "attention_mask", "label"]
)

#load model
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

#compute metrics
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)

    precision, recall, f1, _ = precision_recall_fscore_support(
        labels,
        predictions,
        average="binary"
    )

    acc = accuracy_score(labels, predictions)

    return {
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }

#set evaluation directory and training arguments
EVAL_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "eval_tmp")
training_args = TrainingArguments(
    output_dir=EVAL_DIR,
    per_device_eval_batch_size=32,
    fp16=torch.cuda.is_available(),
)

#trainer
trainer = Trainer(
    model=model,
    args=training_args,
    eval_dataset=test_set,
    compute_metrics=compute_metrics,
)

#evaluate model and print metrics
metrics = trainer.evaluate()

print(metrics)