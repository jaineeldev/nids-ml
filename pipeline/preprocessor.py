# pipeline/preprocessor.py
# -------------------------------------------------------
# OWNER: Jaineel (data cleaning & preparation)
# NOTE FOR NICHOLAS: this output feeds directly
#                    into your ML training pipeline
# -------------------------------------------------------

import pandas as pd
import os

# folder paths
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")


# loads the most recent CSV capture file from the data folder
def load_latest_capture():
    # get all CSV files in the data folder
    csv_files = [f for f in os.listdir(DATA_DIR) if f.startswith("capture_") and f.endswith(".csv")]

    if not csv_files:
        print("[preprocessor] No capture files found in data/")
        return None

    # sort by filename to get the most recent one
    latest = sorted(csv_files)[-1]
    filepath = os.path.join(DATA_DIR, latest)
    print(f"[preprocessor] Loading: {filepath}")
    return pd.read_csv(filepath)


# cleans the raw data and removes rows with missing values
def clean_data(df):
    before = len(df)
    df = df.dropna()
    after = len(df)
    print(f"[preprocessor] Removed {before - after} rows with missing values")
    return df


# encodes text columns into numbers so the ML model can read them
# protocol: TCP=0, UDP=1, Other=2
# NOTE FOR NICHOLAS: ML models only understand numbers, not strings
def encode_features(df):
    protocol_map = {"TCP": 0, "UDP": 1, "Other": 2}
    df["protocol"] = df["protocol"].map(protocol_map)
    # fill any unmapped values with 2 (Other)
    df["protocol"] = df["protocol"].fillna(2)
    print(f"[preprocessor] Encoded protocol column")
    return df


# saves the cleaned and encoded data to a new CSV
def save_processed_data(df, filename="processed.csv"):
    output_path = os.path.join(OUTPUT_DIR, filename)
    df.to_csv(output_path, index=False)
    print(f"[preprocessor] Saved processed data to: {output_path}")
    return output_path


# runs the full preprocessing pipeline
# NOTE FOR NICHOLAS: run this before training your model
def run_preprocessor():
    print("=" * 50)
    print("  Running preprocessor...")
    print("=" * 50)

    df = load_latest_capture()
    if df is None:
        return

    df = clean_data(df)
    df = encode_features(df)
    save_processed_data(df)

    print("=" * 50)
    print("  Preprocessing complete.")
    print("=" * 50)


if __name__ == "__main__":
    run_preprocessor()