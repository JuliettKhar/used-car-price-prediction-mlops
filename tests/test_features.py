from src.features import (
    CATEGORICAL,
    NUMERICAL,
    TARGET,
)


def test_target_is_price():
    assert TARGET == "price"


def test_model_is_in_categorical_features():
    assert "model" in CATEGORICAL


def test_car_age_is_in_numerical_features():
    assert "car_age" in NUMERICAL


def test_no_duplicate_features():
    all_features = CATEGORICAL + NUMERICAL

    assert len(all_features) == len(set(all_features))
