import pandas as pd

def read_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = df.dropna(subset=["brand"])
    df = df.drop(
        columns=[
            "reg_year",
            "has_insurance",
            "title",
        ],
        errors="ignore",
    )

    df["engine_capacity(CC)"] = (
        df["engine_capacity(CC)"]
        .fillna(df["engine_capacity(CC)"].median())
    )
    
    df["car_age"] = 2024 - df["make_year"]

    return df