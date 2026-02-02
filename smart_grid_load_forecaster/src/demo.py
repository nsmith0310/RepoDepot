#import time
import time
#import models
from models import *
#import utilities
from utility import *
#import formatter
from formatter import *
import os, pickle
from pathlib import Path
import gdown


url = 'https://drive.google.com/file/d/19G1c4T7aC3Q2aGBIsU-35FE8ckLsl0XO/view?usp=drive_link'

output_path = '/app/src/model/GB_model.pkl' 

gdown.download(url, output_path, quiet=False, fuzzy=True)

if os.path.exists(output_path):
    print(f"Model successfully downloaded to {output_path}")

#path to sample data
sample_path = os.path.join(os.path.dirname(__file__), "..", "data", "sample.pkl")

#load preprocessed sample data
with open(sample_path, 'rb') as f:
    sample = pickle.load(f)
    
#Gradient Boosting
MODEL_DIR = Path(__file__).parent / "model"

with open(MODEL_DIR / 'GB_model.pkl', 'rb') as f:
    models = pickle.load(f)

X_sample, y_sample = sample 

predictions = predict_gradient_boosting(models,X_sample)

predictions, targets = demo_output(predictions,y_sample)

print()
print("Sample prediction for a single load zone on a single day:")
print()
print("Predicted load (24 hours):")
print(predictions[1][4])
print()
print("Actual load (24 hours):")
print(targets[1][4])
print()
print("Sample R^2 for 162 sample days over 5 load zones:")
sample_r2 = score_gradient_boosting(models,X_sample,y_sample)[0]
print("R^2 = "+str(round(sample_r2,4)))
