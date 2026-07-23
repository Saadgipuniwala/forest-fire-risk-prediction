# FIRELINE — Forest Fire Risk Prediction for Uttarakhand

Predicting forest fire risk in Uttarakhand's highest-risk districts —
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
6. Validated against the 2024 Uttarakhand fire season (April–June) across all four districts —
   the model maintained consistently high risk scores throughout the active season and correctly
   tracked the drop to low risk as conditions cooled in late June, distinguishing active-danger
   months from the calmer period that followed
7. Built a live dashboard (Flask + JavaScript) showing risk by district for any date in the test period

## Results

- **93% recall** on real fires in the 2024 test season (caught 247 of 267 real fire events)
- **ROC AUC: 0.795 | PR AUC: 0.895**
- Feature importance confirmed humidity and precipitation trends as the strongest predictors —
  consistent with known fire-science mechanisms

## Honest Limitations

- Validated against one real fire season (2024, April–June), not multiple independent
  fire years — a promising proof of concept, not an operationally proven system
- The original "3–5 day early warning before a single fire" framing doesn't fully apply —
  the 2024 fire season involved sustained fire activity over months rather than one isolated
  ignition, so validation measures the model's ability to track season-long risk and its
  decline, not lead time before a specific event
- Currently validates against *historical* dates, not live/future forecasts. A natural next step
  would be using Open-Meteo's forecast API (instead of the historical archive) combined with the
  most recent available NDVI reading, to predict real upcoming risk rather than only past dates
- No deep learning (ConvLSTM) attempted — deliberately scoped out given project timeline and no
  prior deep learning experience; documented as future work, not an oversight
- Predicts at district level, not sub-district zones — a reasonable scope for a solo project
  timeline; grid-level prediction (as in the original concept) is a natural next step

## Tech Stack

Python · pandas · scikit-learn · XGBoost · Google Earth Engine · Flask · JavaScript

## Live Demo

Try it here: https://forest-fire-risk-prediction.onrender.com

*(Free-tier hosting — first load may take ~50 seconds if the app has been inactive.)*

## Running Locally
```
pip install -r requirements.txt
cd app
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

## Author

Saadgi Puniwala — B.Tech CSE (Data Science), Dayananda Sagar University
