# NLP Fake news classifier 

## Summary

A Naive Bayes classifier which classifies news articles as real or fake. Includes a pretrained model which obtains near-perfect classification accuracy on a balanced test set of over 8900 samples. Also includes comparisons between Naive Bayes using different features and Logistic Regression using those same features.  

---

## Description

This project was developed to effectively classify news articles as being real or fake. It compares Naive Bayes against Logistic Regression and finds an optimal algorithm and set of features. Naive Bayes was coded from scratch and is ultimately the best-performing method with appropriate feature selection. Please see the notebooks for a more in-depth comparison. The project includes the ability to select different combinations of features (article title, article contents, article subject) as well as other basic preprocessing steps like lowercasing, segmentation, and vectorization. It trains and compares both Naive Bayes and Logistic Regression using the same features and preprocessing steps. The final optimal model - Naive Bayes using only article title - achieves over 99% classification accuracy and a near-perfect ROC curve on a balanced holdout test set of over 8900 samples.

---

## Tech Stack

- Language: Python
- ML / DL: scikit-learn
- Data: Pandas, scikit-learn
- Visualization: Matplotlib
- MLOps / Tools: Git, Docker

---

## Folder Structure
<br>
nlp_fake_news_classifier/<br>
├── src/ # Inference scripts<br>
│ ├── demo.py # Interactive demo<br>
│ ├── inference.py # Run inference on test set using fully trained model<br>
│ ├── logistic_regression_classifier.py # Logistic Regression class<br>
│ ├── naive_bayes_classifier.py # Naive Bayes class<br>
│ ├── train.py # Train Naive Bayes<br>
│ ├── utility.py # Utility library<br> 
│ └── model/ # Pre-trained Naive Bayes model <br>
├── notebooks/ # Showcase and experiments<br>
│ ├── naive_bayes_titles_only.ipynb # Demonstrate Naive Bayes trained on only titles; achieves over 99% classification accuracy<br>
│ └── naive_bayes_vs_logistic_regression.ipynb # Compares Naive Bayes against Logistic Regression each trained on all features<br> 
├── data/ # Instructions and link to download the full dataset<br>
├── Dockerfile # Container for running the interactive demo<br>
├── requirements.txt # Dependencies for running the interactive demo<br>
├── local_requirements.txt # Dependencies for full functionality of all scripts<br>
└── README.md # This file<br>

---

## Demo

Type in a headline and see the prediction for whether it is fake or real news. No dataset required. 

## Quick Start for Docker

1\. Build the Docker image

docker build -t demo .

2\. Run the interactive demo

docker run -it demo

3\. Type any headline and see the model prediction.

---

## Running Locally

1\. Clone the repository

git clone --depth 1 --no-checkout https://github.com/nsmith0310/RepoDepot.git<br>
cd RepoDepot<br>
git sparse-checkout init --cone<br>
git sparse-checkout set nlp_fake_news_classifier<br>
git checkout main<br>

2\. Install dependencies

pip install -r local_requirements.txt

3\. Run script of choice

python demo.py 
python inference.py
python train.py

---

## Notebooks

Showcase high-accuracy Naive Bayes model: naive_bayes_titles_only.ipynb
- Trained on entire dataset
- Achieves over 99% classification accuracy on a test set of over 8900 samples
- Only trained using headlines; ignores article content and subject thereby improving accuracy
- Evaluated using a wide variety of metrics and includes an ROC curve

Compare Naive Bayes against Logistic Regression: naive_bayes_vs_logistic_regression.ipynb
- Both models trained on entire dataset
- Both models trained using article title, subject, and contents
- Evaluated using a wide variety of metrics and includes ROC curves 

---

## Data 

Please see data/README.md
- Dataset is not included but simple instructions for download and use are provided

---

## License

All scripts, notebooks, and models are free to explore for educational purposes 
