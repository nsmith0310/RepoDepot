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



