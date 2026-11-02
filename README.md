# NYC Taxi Trip Duration Prediction

**A reproducible machine learning case study in trip-duration estimation, baseline benchmarking, and time-aware evaluation.**

[Open notebook in Google Colab](https://colab.research.google.com/github/antonypradeep54/Machine-Learning---NYC-taxi-trip-duration-prediction/blob/main/NYC_Taxi_Trip_Duration.ipynb) · [Validation evidence](docs/validation.md)

## Executive summary

**Problem.** Estimating journey duration can support passenger expectations and operational planning in mobility services. This project investigates how well a relatively simple Random Forest predicts NYC taxi trip duration from information available around pickup time.

**Approach.** Train a Random Forest on `log1p(trip_duration)` using passenger count, pickup hour, pickup day of week, and straight-line (Haversine) pickup-to-drop-off distance. Invert predictions with `expm1` before evaluating RMSLE and MAE on the original seconds scale.

**Finding.** On an 80/20 random validation split, the Random Forest achieved **0.509357 RMSLE** and **6.26-minute MAE**, compared with **0.795762 RMSLE** and **9.40-minute MAE** for a training-median baseline. A separate chronological split yielded **0.521922 RMSLE** and **6.43-minute MAE** for the Random Forest.

**Interpretation.** The model improves substantially over a simple baseline on both validation strategies, but long-tail errors remain important. These are owner-reported notebook runs, not independent test-set results or production performance guarantees.

## Evaluation at a glance

All numbers below were reported from a full-dataset Google Colab execution on 2026-11-02, using **729,322 records**. Both validation designs use **583,457 training** and **145,865 validation** records, but they contain different validation examples.

| Validation design | Model | RMSLE ↓ | MAE (minutes) ↓ |
| --- | --- | ---: | ---: |
| Random 80/20 | Training-median baseline | 0.795762 | 9.40 |
| Random 80/20 | Random Forest | **0.509357** | **6.26** |
| Chronological 80/20 | Training-median baseline | 0.811359 | 9.80 |
| Chronological 80/20 | Random Forest | **0.521922** | **6.43** |

Relative to the median baseline, the Random Forest reduced RMSLE by approximately **36.0%** on the random split and **35.7%** on the chronological split. These are **relative reductions in error**, not prediction accuracy percentages.

### Where predictions still struggle

On the chronological validation holdout, the absolute-error distribution was:

| Percentile | Absolute error (minutes) |
| --- | ---: |
| Median / P50 | 2.92 |
| P90 | 10.25 |
| P95 | 14.43 |
| P99 | 28.01 |

**4.6%** of predictions had an absolute error greater than **15 minutes**. This tail matters for customer-facing ETA experiences: average metrics alone would obscure some substantially inaccurate estimates.

## Product and modeling decisions

- **Practical feature set:** Four inputs represent a lightweight starting point rather than an exhaustive ETA system. Haversine distance is not road distance and does not capture traffic, routing, weather, or incidents.
- **Training-only baseline:** A constant median prediction provides a minimum benchmark against which model complexity must justify itself.
- **Two validation strategies:** A reproducible random holdout supports comparison; an additional chronological holdout tests later trips without using future pickup records for training.
- **Interpretable errors:** RMSLE emphasizes relative/log-scale discrepancies, while MAE and error percentiles express the passenger-facing error in minutes.
- **Conservative claims:** The chronological comparison is one holdout experiment, not proof of temporal stability across seasons or a production readiness assessment.

## Reproduce the notebook

1. Clone this repository and create a Python environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Obtain the original `nyc_taxi_trip_duration.csv` dataset used for this project. **Its authoritative download URL, exact version and checksum have not yet been confirmed; do not assume a similarly named public dataset is identical.** The dataset is **not included** in this repository. Place it at `dataset/nyc_taxi_trip_duration.csv`, or upload the file when prompted in Google Colab.
4. Open `NYC_Taxi_Trip_Duration.ipynb` locally or via the Colab link above and run cells in order. A full run trains two 100-tree Random Forest models and may take time on CPU.
5. Compare your printed metrics with the [validation record](docs/validation.md). Results can vary across dataset versions and software environments.

### Expected input fields

The notebook expects a CSV including `pickup_datetime`, `dropoff_datetime`, `pickup_longitude`, `pickup_latitude`, `dropoff_longitude`, `dropoff_latitude`, `vendor_id`, `passenger_count`, and `trip_duration`. Only the selected pickup-time, passenger-count, and coordinate-derived features enter the model. Drop-off timestamps are not used as predictors.

### Environment and checks

Owner-reported execution: Python **3.13.16**, NumPy **2.1.3**, pandas **2.2.3**, scikit-learn **1.6.1**. Dependency ranges are specified in [requirements.txt](requirements.txt), not locked to an exact environment.

The repository's GitHub Actions workflow checks notebook JSON/code-cell syntax and runs a **small synthetic-data Random Forest smoke test**. The smoke test checks the feature schema, training, prediction inversion and metrics. **It does not download the NYC dataset, run the full notebook, or reproduce the reported validation metrics.**

## Limitations and next steps

- The authoritative CSV source URL, checksum, exact upstream dataset version, saved executed notebook, and independent reproduction have not yet been captured.
- Random and chronological validation results are not directly paired because their holdout examples differ.
- A single chronological holdout is not a substitute for repeated rolling-origin or out-of-time evaluation.
- No separate untouched final test set is reported; the results are **validation** metrics only.
- Feature coverage is limited: no road-network distance, live traffic, route selection, weather, or demand conditions.
- Further work could compare simpler regression alternatives, add error breakdowns by trip length/time of day, and evaluate deployment constraints such as latency, drift, and prediction uncertainty.

The historical **0.0739 RMSLE** sometimes associated with this project is **unverified** and is deliberately excluded from performance claims.

## Repository contents

- [NYC_Taxi_Trip_Duration.ipynb](NYC_Taxi_Trip_Duration.ipynb) — exploratory analysis, modeling, baselines, chronological validation, and diagnostics
- [docs/validation.md](docs/validation.md) — reported execution evidence and limitations
- [requirements.txt](requirements.txt) — Python dependencies
- [scripts/validate_dataset.py](scripts/validate_dataset.py) — input dataset validation
- [scripts/smoke_test_model.py](scripts/smoke_test_model.py) — fast synthetic model smoke test
- [.github/workflows/notebook-syntax.yml](.github/workflows/notebook-syntax.yml) — syntax and synthetic model smoke-test CI

## Portfolio takeaway

This project illustrates a product-minded ML evaluation process: **start with a measurable user problem, establish a baseline, test for temporal generalization, inspect failure cases, and communicate limitations without overstating model readiness.**
