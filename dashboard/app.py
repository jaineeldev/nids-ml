# dashboard/app.py
# -------------------------------------------------------
# OWNER: Jaineel (dashboard & visualisation)
# NOTE FOR NICHOLAS: once your model is ready, we can
#                    add a prediction column to the table
# -------------------------------------------------------

from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"))

# path to the processed data file
DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "processed.csv")


# loads the processed CSV and returns it as a list of rows
def load_data():
    if not os.path.exists(DATA_PATH):
        return []
    df = pd.read_csv(DATA_PATH)
    # decode protocol numbers back to readable names for display
    protocol_map = {0: "TCP", 1: "UDP", 2: "Other"}
    df["protocol"] = df["protocol"].map(protocol_map)
    return df.to_dict(orient="records")


# main dashboard route
@app.route("/")
def index():
    packets = load_data()
    total = len(packets)
    tcp = sum(1 for p in packets if p["protocol"] == "TCP")
    udp = sum(1 for p in packets if p["protocol"] == "UDP")
    rendered = render_template("index.html", packets=packets, total=total, tcp=tcp, udp=udp)
    print(f"[debug] rendered length: {len(rendered)}")
    print(rendered[:500])
    return rendered


if __name__ == "__main__":
    app.run(debug=True)