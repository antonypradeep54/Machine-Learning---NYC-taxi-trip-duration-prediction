"""Fast synthetic regression smoke test; no NYC dataset or external downloads required.

Checks feature schema, target transformation, nonnegative predictions and metric
calculation. Does NOT reproduce the full-dataset validation results.
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_log_error
from sklearn.model_selection import train_test_split


def main() -> None:
    rng = np.random.default_rng(42)
    n = 160
    distance = rng.uniform(0.3, 20, size=n)
    frame = pd.DataFrame({
        "passenger_count": rng.integers(1, 5, size=n),
        "pickup_hour": rng.integers(0, 24, size=n),
        "day_of_week": rng.integers(0, 7, size=n),
        "distance": distance,
    })
    duration_seconds = np.maximum(1, 180 + 145 * distance + rng.normal(0, 90, size=n))
    target_log = np.log1p(duration_seconds)
    X_train, X_val, y_train, y_val = train_test_split(
        frame, target_log, test_size=0.2, random_state=42
    )
    model = RandomForestRegressor(n_estimators=10, random_state=42, n_jobs=1)
    model.fit(X_train, y_train)
    predictions = np.clip(np.expm1(model.predict(X_val)), 0, None)
    actual = np.expm1(y_val)
    baseline = np.full(len(actual), np.median(np.expm1(y_train)))
    for name, estimate in (("model", predictions), ("median baseline", baseline)):
        rmsle = float(np.sqrt(mean_squared_log_error(actual, estimate)))
        mae = float(mean_absolute_error(actual, estimate))
        assert np.isfinite(rmsle) and np.isfinite(mae)
        assert rmsle >= 0 and mae >= 0
        assert np.isfinite(estimate).all() and (estimate >= 0).all()
        print(f"{name}: RMSLE={rmsle:.4f}, MAE={mae:.1f} seconds")
    assert len(predictions) == len(X_val) == 32
    print("Synthetic model smoke test passed; no real-data performance claim.")


if __name__ == "__main__":
    main()
