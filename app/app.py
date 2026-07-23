from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv(r"C:\Users\dolly\OneDrive\Desktop\fireline-project\data\processed\dashboard_predictions.csv")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/predictions")
def get_predictions():
    date = pd.Timestamp.today().strftime("%Y-%m-%d")
    dates_available = sorted(df["date"].unique())
    return jsonify({
        "dates_available": dates_available,
        "default_date": dates_available[0]
    })

@app.route("/api/predictions/<date>")
def get_predictions_for_date(date):
    day_data = df[df["date"] == date]
    result = day_data.to_dict(orient="records")
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)