# tests/test_integration.py

import pickle


def test_model_prediction():
    with open("models/dv.pkl", "rb") as f_in:
        dv = pickle.load(f_in)

    with open("models/model.pkl", "rb") as f_in:
        model = pickle.load(f_in)

    car = {
        "brand": "Hyundai",
        "model": "Creta",
        "transmission": "Manual",
        "fuel_type": "Petrol",
        "ownership": "1st owner",
        "spare_key": "Yes",
        "reg_number": "KA01",
        "car_age": 3,
        "engine_capacity(CC)": 1497,
        "km_driven": 30000,
    }

    X = dv.transform([car])

    prediction = model.predict(X)[0]

    assert prediction > 0
