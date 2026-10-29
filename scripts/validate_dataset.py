"""Validate the NYC taxi duration target before model evaluation.

Usage:
    python scripts/validate_dataset.py dataset/nyc_taxi_trip_duration.csv

This script reports potential outliers; it does not drop or alter rows.
"""
from __future__ import annotations

import argparse
import numpy as np
import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", help="Path to nyc_taxi_trip_duration.csv")
    parser.add_argument("--target", default="trip_duration")
    parser.add_argument(
        "--long-trip-hours",
        type=float,
        default=6.0,
        help="Threshold for flagging long trips for review (default: 6 hours)",
    )
    args = parser.parse_args()

    df = pd.read_csv(args.csv_path)
    if args.target not in df.columns:
        raise SystemExit(
            f"Target column {args.target!r} not found. Columns: {list(df.columns)}"
        )

    y = pd.to_numeric(df[args.target], errors="coerce")
    finite = np.isfinite(y.to_numpy(dtype=float))
    positive = y > 0

    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print(f"Missing/non-numeric target: {int(y.isna().sum()):,}")
    print(f"Non-finite target: {int((~finite).sum()):,}")
    print(f"Non-positive target: {int((~positive).sum()):,}")

    valid = y[positive & finite]
    if valid.empty:
        raise SystemExit("No positive finite target values available.")

    round_trip = np.expm1(np.log1p(valid.to_numpy(dtype=float)))
    max_error = float(np.max(np.abs(round_trip - valid.to_numpy(dtype=float))))
    print(f"Duration min (seconds): {valid.min():,.0f}")
    print(f"Duration max (seconds): {valid.max():,.0f}")
    print(f"log1p/expm1 max round-trip error: {max_error:.3g}")
    print("Duration quantiles (seconds):")
    print(valid.quantile([0, 0.50, 0.75, 0.95, 0.99, 0.999, 1.0]).to_string())

    threshold_seconds = args.long_trip_hours * 3600
    flagged = valid[valid > threshold_seconds]
    print(
        f"Trips longer than {args.long_trip_hours:g} hours "
        f"({threshold_seconds:,.0f} seconds): {len(flagged):,}"
    )
    print("These rows are flagged for investigation only; no rows were removed.")


if __name__ == "__main__":
    main()
