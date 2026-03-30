## Logging formats

API log: 
- scraper_log.txt
- format: TIMESTAMP TOTAL_NUMBER_OF_API_CALLS TOTAL_NUMBER_OF_DATABASE_INSERTIONS
- purpose: monitor number of API calls to support Adzuna rate limits and number of freshly added jobs

Filter log:
- filter_log.txt
- format: TIMESTAMP REGEX_POSITIVES REGEX_NEGATIVES BERT_POSITIVES BERT_NEGATIVES
- purpose: monitor number of jobs being filtered at each stage as well as the balance of filtering between the two stages 
