# nids-ml

> 🚧 **Project in active development** — check back for updates.

ML-powered network intrusion detection system built in Python. Captures live network traffic, preprocesses it, and uses machine learning to classify connections as normal or malicious.

## Overview

This project combines cybersecurity and machine learning to detect network intrusions and threats in real time. Built as a collaboration between a Cybersecurity student and a Machine Learning engineer.


## Features

- [x] Live packet capture using Scapy
- [x] Automatic CSV logging of captured traffic
- [x] Data preprocessing and feature encoding pipeline
- [x] Flask web dashboard with auto-refresh
- [x] CLI arguments for flexible capture options
- [x] NSL-KDD dataset integration
- [ ] ML model training and inference (in progress)
- [ ] Live threat prediction on dashboard

## Project structure

```
nids-ml/
├── capture/           # packet capture and logging
│   ├── sniffer.py     # captures live network packets
│   └── logger.py      # saves packets to timestamped CSV
├── pipeline/          # data cleaning and preparation
│   └── preprocessor.py # cleans and encodes CSV data for ML
├── dashboard/         # Flask web dashboard
│   ├── app.py         # Flask app
│   └── templates/
│       └── index.html # dashboard UI
├── training/          # ML model training
├── model/             # saved trained model files
├── notebooks/         # Jupyter notebooks for exploration
├── data/              # datasets and captured CSVs
│   └── KDDTrain+.txt  # NSL-KDD labelled training dataset
├── tests/             # unit tests
├── main.py            # project entry point
└── requirements.txt   # Python dependencies
```

## Getting started

1. Clone the repo:
```bash
git clone https://github.com/jaineeldev/nids-ml.git
cd nids-ml
```

2. Create and activate a virtual environment:
```bash
py -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Npcap (Windows only) for packet capture:
> https://npcap.com/#download

## Usage

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

## Tech stack

| Area | Tools |
|---|---|
| Language | Python 3.11+ |
| Packet Capture | Scapy |
| ML / Data | Scikit-learn, Pandas, NumPy |
| Dashboard | Flask |
| Dataset | NSL-KDD |

## Contributors

| Role | GitHub |
|---|---|
| Cybersecurity & Infrastructure | [@jaineeldev](https://github.com/jaineeldev) |
| Machine Learning & Modelling | [@NicholasNg380](https://github.com/NicholasNg380) |


## License

MIT
