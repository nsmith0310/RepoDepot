## Dataset

The full dataset used for training and evaluation is NOT INCLUDED in this repository due to size and licensing considerations.

The dataset consists of 28 experimental subjects playing 4 different genres of video games while having brain activity measured using 
EEG. The training data consists of these EEG timeseries readings as input and the associated game genre (1-4) as the label for that timeseries. 

A small sample of 5 EEG timeseries recordings (73 timesteps each) has been included already preprocessed. These are contained in

data/sample.pkl

The sample data allow use of demo.py without obtaining the full dataset. Each of the 5 samples were taken from the test set  
and thus were not seen during model training. 

---

## Full Dataset Source

The dataset used in this project can be downloaded from:

https://www.kaggle.com/datasets/sigfest/database-for-emotion-recognition-system-gameemo

please extract the downloaded archive to the data folder such that the directory structure looks like
data/archive/GAMEEMO/...

---

## Expected Format

After downloading, the GAMEEMO folder should contain 29 subfolders, 28 of which are the individual experimental subjects from which
the EEG recordings were taken. The GAMEEMO/Gameplays can be ignored, but an example of what each of the m 28 subject directories should look like is:

Sm/
├── Preprocessed EEG Data/ 
│ ├── .csv format/ 
│    ├── SmG1AllChannels.csv
│    ├──  ...
│    └── SmG4AllChannels.csv
│ └── .mat format/ 
│    ├── SmG1AllChannels.mat
│    ├──  ...
│    └── SmG4AllChannels.mat
├── Raw EEG Data/ 
│ ├── .csv format/ 
│    ├── SmG1AllRawChannels.csv
│    ├──  ...
│    └── SmG4AllRawChannels.csv
│ └── .mat format/ 
│    ├── SmG1AllRawChannels.mat
│    ├──  ...
│    └── SmG4AllRawChannels.mat
└──  SAM Ratings
     ├── G1.pdf
     ├──  ...
     └── G4.pdf

---


