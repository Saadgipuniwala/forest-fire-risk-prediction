from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "dashboard_predictions.csv")

df = pd.read_csv(CSV_PATH)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/predictions")
def get_predictions():
    dates_available = sorted(df["date"].unique())
    return jsonify({
        "dates_available": dates_available,
        "default_date": dates_available[0]
    })

@app.route("/api/predictions/<date>")
def get_predictions_for_date(date):
    day_data = df[df["date"] == date]
    result = day_data.to_dict(orient="rec