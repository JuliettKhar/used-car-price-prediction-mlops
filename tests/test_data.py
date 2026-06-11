import pandas as pd

from src.data import clean_data


def test_clean_data_removes_empty_brand_row():
    df = pd.DataFrame([
        {
            "brand": "Toyota",
            "model": "Corolla",
            "transmission": "Manual",
            "make_year": 2020,
            "reg_year": None,
            "fuel_type": "Petrol",
            "engine_capacity(CC)": 1200,
            "km_driven": 30000,
            "ownership": "1st owner",
            "price": 600000,
            "overall_cost": 12000,
            "has_insurance": True,
            "spare_key": "Yes",
            "reg_number": "KA01",
            "title": "2020 Toyota Corolla",
        },
        {
            "brand": None,
            "model": None,
            "transmission": None,
            "make_year": None,
            "reg_year": None,
            "fuel_type": None,
            "engine_capacity(CC)": None,
            "km_driven": None,
            "ownership": None,
            "price": 1883558000,
            "overall_cost": None,
            "has_insurance": None,
            "spare_key": None,
            "reg_number": None,
            "title": None,
        },
    ])

    result = clean_data(df)

    assert len(result) == 1
    assert result.iloc[0]["brand"] == "Toyota"


def test_clean_data_creates_car_age():
    df = pd.DataFrame([
        {
            "brand": "Toyota",
            "model": "Corolla",
            "transmission": "Manual",
            "make_year": 2020,
            "fuel_type": "Petrol",
            "engine_capacity(CC)": 1200,
            "km_driven": 30000,
            "ownership": "1st owner",
            "price": 600000,
            "spare_key": "Yes",
            "reg_number": "KA01",
        }
    ])

    result = clean_data(df)

    assert "car_age" in result.columns
    assert result.iloc[0]["car_age"] == 4