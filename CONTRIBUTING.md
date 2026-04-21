# Contributing to nids-ml

This document is primarily for **Nicholas Ng** (@NicholasNg380) — it explains the project structure, how to get set up, and exactly what needs to be built on the ML side.


## Project structure

```
nids-ml/
├── capture/           # Jaineel — packet capture and logging
│   ├── sniffer.py     # captures live network packets
│   └── logger.py      # saves packets to CSV
├── pipeline/          # Jaineel — data cleaning and preparation
│   └── preprocessor.py # cleans and encodes CSV data for ML
├── dashboard/         # Jaineel — Flask web dashboard
│   ├── app.py         # Flask app
│   └── templates/
│       └── index.html # dashboard UI
├── training/          # Nicholas — ML model training (your folder)
├── model/             # Nicholas — save your trained model here
├── notebooks/         # shared — Jupyter notebooks for exploration
├── data/              # shared — datasets and captured CSVs
│   └── KDDTrain+.txt  # NSL-KDD labelled training dataset
├── tests/             # shared — unit tests
├── main.py            # entry point — run this to start the NIDS
└── requirements.txt   # Python dependencies
```

## Getting set up

1. Clone the repo to your Desktop:

Windows:
```bash
git clone https://github.com/jaineeldev/nids-ml.git %USERPROFILE%\Desktop\nids-ml
```

Mac/Linux:
```bash
git clone https://github.com/jaineeldev/nids-ml.git ~/Desktop/nids-ml
```

2. Go into the folder:
```bash
cd Desktop/nids-ml
```

3. Create a virtual environment:
```bash
py -m venv venv
```

4. Activate it:
```bash
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

5. Install dependencies:
```bash
pip install -r requirements.txt
```

6. Create your branch:
```bash
git checkout -b feature/model-training
git push origin feature/model-training
```

## Syncing with main before each session

Always run these before starting work:

```bash
git checkout main
git pull origin main
git checkout feature/model-training
git merge main
```

## Running the project

Capture packets and preprocess:
```bash
py main.py
```

With options:
```bash
py main.py --count 100
py main.py --count 50 --interface WiFi
py main.py --count 20 --no-preprocess
```

Run the dashboard:
```bash
py dashboard/app.py
```

Then open http://127.0.0.1:5000 in your browser.


## What Nicholas needs to build

Your folder is `training/`. Here's what needs to be done:

### 1. training/model.py

Train an ML classifier on the NSL-KDD dataset (data/KDDTrain+.txt).

The dataset has 42 columns. The second to last column is the label (normal, neptune, smurf etc.) and the last column is a difficulty score.

Suggested approach:
- Load KDDTrain+.txt with pandas
- Encode categorical columns
- Train a Random Forest or XGBoost classifier
- Evaluate with accuracy, precision, recall and confusion matrix
- Save the trained model to model/nids_model.pkl using joblib

### 2. pipeline/predictor.py

Once the model is trained, build a predictor that:
- Loads the saved model from model/nids_model.pkl
- Takes data/processed.csv as input
- Outputs a prediction column (normal or attack) for each row
- Saves the result to data/predictions.csv

### 3. Connect to the dashboard

Once predictions are working, let Jaineel know and he will add a Prediction column to the dashboard table.


## Branch and PR workflow

- Never commit directly to main
- Create feature branches: git checkout -b feature/your-feature
- Push your branch: git push origin feature/your-feature
- Open a Pull Request on GitHub when the feature is ready
- Tag @jaineeldev for review

## Questions?

Reach out to me (Jaineel) directly or open a GitHub Issue on the repo.