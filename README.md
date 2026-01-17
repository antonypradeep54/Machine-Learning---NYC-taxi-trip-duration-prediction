# NYC Taxi Trip Duration

Short description
Predict taxi trip duration for NYC trips using timestamp and coordinate features and a Random Forest regression model.

Table of contents
- Dataset
- Installation
- Usage
- Features & methods
- Evaluation
- Notes & License

Dataset
Place the CSV at: `dataset/nyc_taxi_trip_duration.csv`  
Expected file: `nyc_taxi_trip_duration.csv` (columns: pickup_datetime, dropoff_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, vendor_id, passenger_count, trip_duration)

Installation
1. Create and activate a virtual environment (recommended)
2. Install dependencies:
   pip install -r requirements.txt

Usage
- Jupyter: open the notebook and run cells.
- Google Colab: upload the CSV or use the included `files.upload()` snippet to move the file into `dataset/`.

Features & methods
- Data cleaning: convert pickup/dropoff to datetime, extract hour/day/week/month.
- Feature engineering: haversine distance, passenger_count, pickup_hour, day_of_week.
- Hypothesis test: two-sample t-test to compare vendor trip durations.
- Model: RandomForestRegressor trained on log-transformed trip duration (`log1p`).

Evaluation
- Metric: Root Mean Squared Log Error (RMSLE).
- Example result (from sample run): Validation RMSLE ≈ 0.0739 (excellent).

