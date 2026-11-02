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

The reported split is consistent with 80/20 random splitting. These are observed validation metrics, **not** test-set performance or a production accuracy guarantee. The dataset checksum, Colab execution artifact and independent rerun are not yet recorded. The old 0.0739 RMSLE remains unverified. Package 03 baseline, chronological comparison and error diagnostics are recorded below.

## Package 03 comparisons (owner-reported, 2026-11-02)

All values below were supplied from Google Colab by the project owner. Independent rerun remains outstanding; chronological absolute-error diagnostics are recorded below. Both splits use 583,457 training and 145,865 validation records; the random and chronological validation sets differ.

| Validation split | Model | RMSLE (duration seconds scale) | MAE (minutes) |
| --- | --- | ---: | ---: |
| Random 80/20 | Training-median baseline | 0.795762 | 9.40 |
| Random 80/20 | Random Forest | 0.509357 | 6.26 |
| Chronological 80/20 | Training-median baseline | 0.811359 | 9.80 |
| Chronological 80/20 | Random Forest | 0.521922 | 6.43 |

The Random Forest improves RMSLE over the median baseline by approximately 36.0% on the random split and 35.7% on the chronological split. Chronological Random Forest RMSLE is approximately 2.5% higher than the random-split value, but the validation samples differ. These are holdout validation results, not independent test or production results. Do not claim that temporal robustness is established by this single split.

## Package 03 chronological absolute-error diagnostics (owner-reported, 2026-11-02)

| Measure | Absolute error (minutes) |
| --- | ---: |
| 50th percentile | 2.924140 |
| 90th percentile | 10.253924 |
| 95th percentile | 14.427540 |
| 99th percentile | 28.006947 |

Percentage of chronological validation predictions with absolute error exceeding 15 minutes: **4.6%**. These diagnostics are descriptive, are based on the single chronological holdout, and are not production performance claims. Independent rerun remains outstanding.
