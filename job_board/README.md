# ML-Powered Job Board


## Summary
 
A personal job board that scrapes listings from the Adzuna API, filters them using a process including fine-tuned ModernBERT classifier, and presents them in a browser UI organized by role (Machine Learning Engineer, Software Engineer, Data Scientist) and supporting model feedback.

---

## Description

This project was developed to aid with finding Machine Learning Engineer and adjacent jobs. To standard job search engines, this project adds filtering of irrelevant results (e.g. industrial engineer) which are frequently returned by searches. It utilizes Adzuna API to scrape jobs from three distinct queries - Machine Learning Engineer, Software Engineer, Data Scientist - before filtering those results in a two-stage process and loading the results into a database feeding into a browser-based UI. The filtering is done first using RegEx to ignore jobs with titles from a blacklist. The second stage of the filtering is done using ModernBERT which classifies as either relevant or irrelevant those jobs which passed the first filter. Those jobs which pass both stages get loaded into a database after deduplication measures have been applied. The UI allows for browsing the three categories, reading information about the job, and navigating to the original Adzuna listing. The results are shows to the user sorted in ascending order by years of experience, and descending order by post-date as it is aimed for seeking new, entry-level positions. The UI also provides the ability to delete jobs from the database, mark them as relevant, and as irrelevant. Those marked as relevant and irrelevant can then be used to further fine-tune ModernBERT. 

---

## ModernBERT (Transformers)

Training: Utilizes active learning to begin with. I created a script which allows for hand-labeling a small number of jobs for initial training data and final testing data. These were scraped using a wide variety of search queries in order to expose the model to many variations on relevant and irrelevant jobs. The model was trained using this small (300 balanced samples) dataset. It was then given another larger balanced but unlabeled dataset to run predictions on. Those predictions with low confidence were hand-labeled, combined with the original 300 for a total of about 450, and the model was retrained from scratch to achieve a final F1 of about .93. 

Feedback-based fine-tuning:

The UI allows marking jobs as relevant or irrelevant and these jobs can be used to further fine-tune the model. They are combined with the original 450 training samples, and then used to fine-tune the existing model. The onus is on the user to ensure the new data is balanced where the aim is mainly to spot irrelevant jobs that passed the filtering, and select a relevant one for every irrelevant one they see. The number of irrelevant jobs is very small relative to the 450 initial samples, so oversampling is performed on the new samples so that the new jobs are about 5% of the total dataset size. Due to space constraints, a roll-back model is not maintained, and instead, the feedback-based fine-tuning uses a smaller number of epochs and learning rate than the initial training.

---

## Tech Stack

- Language: Python
- ML / DL: PyTorch, Transformers
- Data: Pandas
- MLOps / Tools: Git, Docker

---

## Folder Structure
<br>
job_board/<br>
├── src/ # Scripts <br>
│ ├── app.py # UI job board browser <br>
│ ├── job_scraper.py # Scrape jobs, filter, load into database <br>
│ ├── filtering.py # Two stage filtration <br>
│ ├── model_tuning.py # Fine-tune model using user feedback <br>
│ ├── model_evaluate.py # Evaluate current model <br>
│ ├── model_data_grabber.py # Obtain initial training data <br>
│ ├── model_dataset_builder.py # Build original training and test sets <br>
│ ├── model_trainer_v1.py # Initial training script <br>
│ ├── dataset_labeler.py # Second training set builder <br>
│ ├── model_trainer_v2.py # Final training script <br>
│ └── db.py # Database helper script <br>
├── data/ # Datasets stored as pickle files <br>
├── models/ # Both models used for active learning <br>
│ ├── ml_job_classifier_v1/ # Initial trained model <br>
│ └── ml_job_classifier_v2/ # Final trained model; target of later feedback fine-tuning <br>
├── logging/ # Log files from scraper <br>
│ ├── filter_log.txt # Log number of RegEx positives/negatives and ModernBERT positives/negatives <br>
│ ├── scraper_log.txt # Log number of calls to API and jobs scraped <br>
│ └── README.md # Explains logging format <br>
├── text/ # Text files used to support functionality; also where relevant/irrelevant JSON populates <br>
│ ├── blacklist.txt # Used by RegEx filter to eliminate irrelevant jobs <br>
│ ├── deleted_hashes.txt # Used to track deleted hashes so subsequent scrapes dont reload them <br>
│ └── job_titles.txt # Used to build training datasets <br>
├── html/ # Store UI template for UI <br>
│ └── template.html # HTML template <br>
├── db/ # Store database <br>
│ └── jobs.db # Database <br>
├── Dockerfile # Container for running the interactive demo <br>
├── requirements.txt # Dependencies for running the interactive demo <br>
├── additional_requirements.txt # Dependencies for full functionality of all scripts <br>
└── README.md # This file <br>

---

## Demo

Interact with database through the UI

## Quick Start for Docker

Note: The database is a limited snapshot from a particular time and some of the jobs in the database may have been delisted by Adzuna.

1\. Build the Docker image

docker build -t job-board .

2\. Run the demo

docker run -p 5000:5000 job-board

Note: if prompted, please allow permission

3\. View the demo

open a web browser and navigate to http://localhost:5000

Usage: 
Click any job row to view its full details in the panel at the top.
Use the Del, Irrelevant, and Relevant checkboxes to mark jobs.
Click Apply Changes to commit your selections.
Use Prev / Next to page through listings within each category.

4\. End the demo

press CTRL+C

Note: You may have to press this multiple times. 

---

## Running Locally

1\. Clone the repository

git clone --depth 1 --no-checkout https://github.com/nsmith0310/RepoDepot.git<br>
cd RepoDepot<br>
git sparse-checkout init --cone<br>
git sparse-checkout set job_board<br>
git checkout main<br>

2\. Install dependencies

pip install -r local_requirements.txt

3\. Run script of choice

Note: You must supply job_scraper.py and model_data_grabber.py with an Adzuna API key. These were originally used directly in the scripts as this project is intended for personal use.

---

## Data 

Please see data/README.md
- Dataset is included as it is sufficiently small.

---

## Model

Please see src/model/README.md
- Trained models are not included in the repository due to file size limitations.

---

## License

All content is free to explore for educational purposes. 

---
