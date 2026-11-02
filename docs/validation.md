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
The project owner has now completed a full-dataset Colab run; see the reported evidence below. Independent reproduction remains outstanding. Do not reuse the historical 0.0739 RMSLE.

## Full-dataset Google Colab execution (reported 2026-11-02)

Execution evidence supplied by the project owner from Google Colab (not independently rerun by the reviewer):

| Item | Value |
| --- | --- |
| Python | 3.13.16 |
| NumPy | 2.1.3 |
| pandas | 2.2.3 |
| scikit-learn | 1.6.1 |
| Dataset rows | 729,322 |
| Training rows | 583,457 |
| Validation rows | 145,865 |
| Model | RandomForestRegressor(n_jobs=-1, random_state=42) |
| Validation RMSLE (seconds scale) | 0.509357 |
| Validation MAE | 375.72 seconds (6.26 minutes) |

The reported split is consistent with 80/20 random splitting. These are observed validation metrics, **not** test-set performance or a production accuracy guarantee. The dataset checksum, Colab execution artifact and independent rerun are not yet recorded. The old 0.0739 RMSLE remains unverified. Baseline and chronological comparisons are deferred to Package 03.
