import os
import pickle
import pandas as pd

from evidently import Report
from evidently.presets import DataDriftPreset

from data import read_data, clean_data
from features import CATEGORICAL, NUMERICAL


def prepare_dataset(df: pd.DataFrame, dv, model) -> pd.DataFrame:
    dicts = df[CATEGORICAL + NUMERICAL].to_dict(orient="records")
    X = dv.transform(dicts)
    result = df[CATEGORICAL + NUMERICAL].copy()
    result["prediction"] = model.predict(X)

    return result


def run_monitoring():
    df = read_data("data/pre-owned cars.csv")
    df_clean = clean_data(df)

    reference_df = df_clean[df_clean["make_year"] <= 2021].copy()
    current_df = df_clean[df_clean["make_year"] > 2021].copy()

    with open("models/dv.pkl", "rb") as f_in:
        dv = pickle.load(f_in)

    with open("models/model.pkl", "rb") as f_in:
        model = pickle.load(f_in)

    reference = prepare_dataset(reference_df, dv, model)
    current = prepare_dataset(current_df, dv, model)

    report = Report(
        [
            DataDriftPreset(),
        ]
    )

    snapshot = report.run(
        reference_data=reference,
        current_data=current,
    )

    os.makedirs("reports", exist_ok=True)
    snapshot.save_html("reports/data_drift_report.html")

    print("Monitoring report saved to reports/data_drift_report.html")


if __name__ == "__main__":
    run_monitoring()
