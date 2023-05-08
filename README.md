# Verification and Extension of Suicide Risk Severity Assessment
Nick Chun and Steven Injety \
\
CS 598 Deep Learning for Healthcare \
Spring 2023

## Data
The annotated data and sample external features file are located in the ./data folder.

## Runtime Requirements
- Python 3.9
- sklearn
- keras
- gensim
- numpy
- nltk

## How to run
- Clone the repository to your machine.
- Download the English-only ConceptNet word embeddings from [https://github.com/commonsense/conceptnet-numberbatch] and place the file in the ./data folder.
- Modify the parameters in the models to your liking.
- Ensure the file paths for each of the 3 data files are correct. (External_Features.csv, english_conceptnet.txt, 500_Reddit_users_posts_labels.csv)
- Change directory by running the command ```cd models```.
- Run each of the models with ```python 5-label.py```, ```python 4-label.py```, etc.

## Citation
Manas Gaur, Amanuel Alambo, Joy Prakash Sain, Ugur Kursuncu, Krishnaprasad Thirunarayan, Ramakanth
Kavuluru, Amit Sheth, Randy Welton, and Jyotishman Pathak. 2019. [Knowledge-aware assessment
of severity of suicide risk for early intervention](https://doi.org/10.1145/3308558.3313698). In The World Wide Web Conference, WWW ’19, page
514–525, New York, NY, USA. Association for Computing Machinery.

Link to original paper's repository: [https://github.com/jpsain/Suicide-Severity]