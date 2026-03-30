# Bidirectional GRU EEG Timeseries Classifier

## Summary

A Bidirectional GRU EEG timeseries classifier that classifies data into four possible video game genres. Trained on EEG data and game genre labels from 28 experimental subjects playing video games while having brain activity recorded.  

---

## Description

This project was developed to classify EEG timeseries data. It utilized the GAMEEMO dataset which consists of 28 human subjects playing 4 different video games of different genres while having their brain activity measured using EEG. The project utilized a bidirectional GRU model to classify 73 timesteps of EEG output into one of the four genres. It includes a framework for selecting different types of data preprocessing techniques such as standardization and normalization, as well as the ability to choose degree of dimensionality reduction via PCA. It also includes basic feature engineering by allowing specification of combinations of EEG channels. The bidirectional GRU (an improvement on recurrent neural networks) is trained with validation-based early stopping. The final trained network was evaluated on holdout testing data, achieving an accuracy of about 87% in determining which game the subject was playing.

---

## Tech Stack

- Language: Python
- ML / DL: TensorFlow, Keras
- Data: NumPy, Pandas, scikit-learn
- Visualization: Matplotlib
- MLOps / Tools: Git, Docker

---

## Folder Structure
<br>
eeg_signal_classifier/<br>
├── src/ # Inference scripts<br>
│ ├── demo.py # Demo<br>
│ ├── inference.py # Run inference on test set using fully trained model<br>
│ ├── train.py # Retrain model<br>
│ ├── preprocess.py # Preprocessing script<br> 
│ └── model/ # Pre-trained model<br>
├── data/ # Instructions and link to download the full dataset<br>
│   ├── sample.pkl #sample of test set for demo<br>
│   └── README.md #instructions for downloading and using full dataset<br>
├── Dockerfile # Container for running the demo<br>
├── requirements.txt # Dependencies for running the demo<br>
├── local_requirements.txt # Dependencies for full functionality of all scripts<br>
└── README.md # This file<br>

---

## Demo

Observe trained model classify sample from holdout test set; no dataset required.

## Quick Start for Docker

1\. Build the Docker image

docker build -t demo .

2\. Run the demo

docker run -it demo

---

## Running Locally

1\. Clone the repository

git clone --depth 1 --no-checkout https://github.com/nsmith0310/RepoDepot.git<br>
cd RepoDepot<br>
git sparse-checkout init --cone<br>
git sparse-checkout set eeg_signal_classifier<br>
git checkout main<br>

2\. Install dependencies

pip install -r local_requirements.txt

3\. Run script of choice

python demo.py 
python inference.py
python train.py 

---

## Data 

Please see data/README.md
- Dataset is not included but simple instructions for download and use are provided

---

## License

All scripts, notebooks, and models are free to explore for educational purposes 



