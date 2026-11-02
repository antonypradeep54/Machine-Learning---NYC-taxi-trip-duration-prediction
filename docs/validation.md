# Package 02 validation checklist

## Dataset
- Obtain the original `nyc_taxi_trip_duration.csv` from the project dataset source.
- Place it at `dataset/nyc_taxi_trip_duration.csv` (not committed to Git).
- Run `python scripts/validate_dataset.py dataset/nyc_taxi_trip_duration.csv`.
- Record row count, missing/non-positive durations, extreme-duration counts and source/version.

## Execution
- Create a fresh Python environment and install `pip install -r requirements.txt`.
- Open `NYC_Taxi_Trip_Duration.ipynb` and run all cells from top to bottom.
- Confirm no errors and record Python, pandas, NumPy and scikit-learn versions.
- Confirm only pickup-time and intended-destination information is used in training.
- Record split configuration, validation RMSLE on seconds scale, and MAE in seconds.
- Compare against a simple baseline in Package 03 before making quality claims.

## Status
The corrected model has **not** been rerun in this pull request. No verified model score is available. Do not reuse the historical 0.0739 RMSLE.
