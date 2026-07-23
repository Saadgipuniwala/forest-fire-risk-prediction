# FIRELINE — Forest Fire Risk Prediction for Uttarakhand

Predicting forest fire risk in Uttarakhand's highest-risk districts, days before ignition —
not just detecting fires after they've already started.

## The Problem

India's existing Forest Fire Alert System (FSI) detects fires using satellite heat sensors —
but only *after* a fire has already ignited, and its broader Fire Danger Rating updates only
once a week. There is no publicly available system that predicts, at a daily and district
level, where a fire is likely to start *before* it does.

## What This Project Does

FIRELINE trains a machine learning model on 5 years of real weather, vegetation dryness (NDVI),
and terrain data to predict fire risk for four of Uttarakhand's highest fire-risk districts:
**Pauri Garhwal, Chamoli, Almora, and Nainital**.

## Data Sources

| Source | Data | Coverage |
|---|---|---|
| NASA FIRMS (VIIRS) | Historical fire detections | 2020–2024, April–June |
| Open-Meteo | Temperature, humidity, rainfall, wind | 2020–2024, April–June |
| Google Earth Engine (MODIS) | NDVI (vegetation dryness) | 2020–2024, April–June |
| Google Earth Engine (SRTM) | Elevation, slope | Static per district |

## Approach

1. Pulled and merged all four data sources by district and date
2. Engineered features: days since last rain, 7-day rolling temperature/humidity averages, NDVI trend
3. Labeled every district-day as fire / no-fire (not just fire points — a real binary classification dataset)
4. Trained and compared two models: **Random Forest** (chosen) and XGBoost
5. Evaluated using confusion matrix, precision/recall, ROC and PR curves
6. **Validated against a real 2024 fire event** in Pauri Garhwal — the model showed rising
   risk probability in the days *before* the fire, tracking a real humidity drop
7. Built a live dashboard (Flask + JavaScript) showing risk by district for any date in the test period

## Results

- **93% recall** on real fires in the 2024 test season (caught 247 of 267 real fire events)
- **ROC AUC: 0.795 | PR AUC: 0.895**
- Feature importance confirmed humidity and precipitation trends as the strongest predictors —
  consistent with known fire-science mechanisms

## Honest Limitations

- Validated against one real historical event and one held-out season, not multiple independent
  fire seasons — a promising proof of concept, not an operationally proven system
- Currently validates against *historical* dates, not live/future forecasts. A natural next step
  would be using Open-Meteo's forecast API (instead of the historical archive) combined with the
  most recent available NDVI reading, to predict real upcoming risk rather than only past dates
- No deep learning (ConvLSTM) attempted — deliberately scoped out given project timeline and no
  prior deep learning experience; documented as future work, not an oversight

## Tech Stack

Python · pandas · scikit-learn · XGBoost · Google Earth Engine · Flask · JavaScript

## Running Locally


pip install -r requirements.txt
cd app
python app.py


Then open `http://127.0.0.1:5000` in your browser.

## Author

Saadgi Puniwala — B.Tech CSE (Data Science), Dayananda Sagar University