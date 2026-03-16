## NLP Fake news classifier 

A Naive Bayes classifier which classifies news articles as real or fake. Includes a pretrained model which obtains near-perfect classification accuracy on a balanced test set of over 8900 samples. Also includes comparisons between Naive Bayes using different features and Logistic Regression using those same features.  

This project highlights:
- Model evaluation: achieves over 99% classification accuracy on a balanced dataset of over 8900 samples
- Comparison experiments between Naive Bayes and Logistic Regression (see notebooks)
- Clean, production-like structure

---

## Features
- Interactive inference demo: type in a headline and see the prediction instantly; no dataset required
- Reproducible experiments: comparison between Naive Bayes and Logistic Regression model; showcase of Naive Bayes model achieving high accuracy 
  using only article titles 
- Trainer allowing for basic feature engineering experimentation (e.g. using just article titles, or article titles and content)

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
