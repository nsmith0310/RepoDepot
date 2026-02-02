## Dataset

The full dataset used for training and evaluation is NOT INCLUDED in this repository due to size and licensing considerations.

---

## Dataset Source

The dataset used in this project can be downloaded from:

Load measurements: https://drive.google.com/file/d/1YHPWYDDDNpuY43MSgHmokm4rjH3UR1uL/view?usp=drive_link
-Load_history_final.csv
Temperature measurements: https://drive.google.com/file/d/1l9ptvj6eO3GlQ_nsOKikvAQt4mkIoM5c/view?usp=drive_link
-Temp_history_final.csv

Please download both .csv files

---

## Expected Format

After downloading, the dataset is expected to contain the following fields:

- 'zone_id' (for Load_history_final.csv) or 'station_id' (Temp_history_final.csv) - the measurement station identifier (integer)
- 'year' year of measurement (integer)
- 'month' month of measurement (integer)
- 'day' day of measurement (integer)
- 'h1' ... 'h24' measurement for each hour of the day

---

## Local Usage (Optional)

If you wish to run training, inference or experiments on the full dataset locally, place the downloaded files in the data folder





