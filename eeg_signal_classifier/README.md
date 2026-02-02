## Bidirectional GRU EEG timeseries classifier

A Bidirectional GRU EEG timeseries classifier that classifies data into four possible video game genres. Trained on EEG data and game genre labels from 28 
experimental subjects playing video games while having brain activity recorded.  

This project highlights:
- Model evaluation: achieves over 87% classification accuracy on holdout data
- Experimentation: includes a framework for feature engineering including EEG channel combinations, principle component analysis, and more
- Clean, production-like structure 

---

## Features
- Inference demo: observe trained model classify sample from original test set; no dataset required
- Trainer allowing feature engineering experimentation
- Evaluation of classification performance on holdout data 

---

## Folder Structure

eeg_signal_classifier/
├── src/ # Inference scripts
│ ├── demo.py # Demo
│ ├── inference.py # Run inference on test set using fully trained model
│ ├── train.py # Retrain model
│ ├── preprocess.py # Preprocessing script 
│ └── model/ 
│   └── model_weights.weights.h5 # Pre-trained model
├── data/ # Instructions and link to download the full dataset
│   ├── sample.pkl #sample of test set for demo
│   └── README.md #instructions for downloading and using full dataset
├── Dockerfile # Container for running the demo
├── requirements.txt # Dependencies for running the demo
├── local_requirements.txt # Dependencies for full functionality of all scripts
└── README.md # This file

---

## Quick Start for Docker

1. Build the Docker image

docker build -t demo .

2. Run the demo

docker run -it demo

---

## Running Locally

1. Clone the repository

git clone --depth 1 --no-checkout https://github.com/nsmith0310/RepoDepot.git
cd RepoDepot
git sparse-checkout init --cone
git sparse-checkout set eeg_signal_classifier
git checkout main

2. Install dependencies

pip install -r local_requirements.txt

3. Run script of choice

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



