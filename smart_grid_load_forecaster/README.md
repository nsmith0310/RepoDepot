# Gradient Boosting Time-Series Load Forecaster - Smart Grid

## Summary

A Gradient Boosting regressor system for smart grid load prediction. Uses historical temperatures and loads to predict the load for different load measurement stations over 24 hours and multiple days. Compares performance of a Gradient Boosting regressor system against a KNN regressor system. 

---

## Description

This project was designed to predict smart grid load demand based on historical (timeseries) temperatures and load values using real-world data. It compares gradient boosting and KNN regression, with gradient boosting ultimately performing better. Please see notebooks for a more in-depth comparison. The project first automatically searches for an optimal mapping between temperature measurement stations and load zones. It then uses this mapping to assign historical temperature measurements to load measurements. It includes a complex feature engineering, preprocessing, and formatting framework which trains 24 models (one for each hour of the day load is to be predicted for on multiple load zones) and combines their output. Feature engineering includes the flexibility to select from various combinations of additional features like fiscal quarter or whether the day falls on a weekend. The final gradient boosting model achieves an R^2 of about .87 on withheld testing data.

---

## Tech Stack

- Language: Python
- ML / DL: scikit-learn
- Data: NumPy, Pandas, scikit-learn
- MLOps / Tools: Git, Docker

---

## Folder Structure

smart_grid_load_forecaster/<br>
├── src/ # Training and inference scripts<br>
│ ├── demo.py # Demo<br>
│ ├── gb_inference.py # Run inference on test set using fully trained Gradient Boosting model<br>
│ ├── knn_inference.py # Run inference on test set using fully trained KNN model<br>
│ ├── gb_train.py # Train Gradient Boosting model<br>
│ ├── knn_train.py # Train KNN model<br>
│ ├── models.py # Model wrapper script <br>
│ ├── map_tune.py #Script for hyperparameter and temperature station to load zone mapping search<br>
│ ├── formatter.py # Library for formatting dataset<br>
│ ├── utility.py # Utility library<br>
│ └── model/ # directory to store models <br>
│ |  └── README.md #Instructions for downloading both trained Gradient Boosting and KNN models<br>
├── notebooks/ # Showcase and experiments<br>
│ └── gradient_boosting_vs_knn.ipynb #Compare Gradient Boosting and KNN <br>
├── data/ <br>
│ ├── sample.pkl #sample of dataset used for demo.py<br>
│ └── README.md # Instructions and link to download the full dataset<br>
├── Dockerfile # Container for running the demo<br>
├── requirements.txt # Dependencies for running the demo<br>
├── local_requirements.txt # Dependencies for full functionality of all scripts<br>
└── README.md # This file<br>

---

## Demo

Showcases trained Gradient Boosting model output for one smart grid load zone over a 24 hour period on one day, comparing output to known load for that
time period, and calculating R^2 for a small sample of the dataset not seen during training

## Quick Start for Docker

1\. Build the Docker image

docker build -t demo .

2\. Run the interactive demo

Note: the demo will download the pretrained Gradient Boosting model into the Docker container

docker run -it demo

---

## Running Locally

1\. Clone the repository

git clone --depth 1 --no-checkout https://github.com/nsmith0310/RepoDepot.git<br>
cd RepoDepot<br>
git sparse-checkout init --cone<br>
git sparse-checkout set smart_grid_load_forecaster<br>
git checkout main<br>

2\. Install dependencies

pip install -r local_requirements.txt

3\. Run script of choice

python demo.py 
python gb_inference.py
python knn_inference.py
python gb_train.py
python knn_train.py

---

## Notebooks

Showcase performance of Gradient Boosting and KNN across training, validation and testing: gradient_boosting_vs_knn.ipynb
- Trains, validates, and tests both models on full data set
- Displays metrics for both models across entire training-validation-testing pipeline, including execution time, R^2, and RPE
- Displays the top 10 worst predictions on the test set made by both models according to relative percentage error (RPE)

---

## Data 

Please see data/README.md
- Dataset is not included but simple instructions for download and use are provided

---

## Model

Please see src/model/README.md
- Trained models are not included in the repository due to file size limitations but simple instructions for download and use are provided

---

## License

All scripts, notebooks, and models are free to explore for educational purposes 



