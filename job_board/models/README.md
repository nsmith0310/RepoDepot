## Models

ModernBERT

Both models are NOT INCLUDED due to size. Please run their respective trainers to both download and train them

Initial model: ml_job_classifier_v1
- Model that is trained with initial balanced dataset of 300 samples

Second model: ml_job_classifier_v2
- Model that is trained with the initial balanced dataset plus additional low-confidence labeled examples from initial model output
- This model is the target of feedback-based finetuning
- Does not use rollback due to size; instead, additional finetuning utilizes a lower number of epochs and learning rate than the 
  initial training 