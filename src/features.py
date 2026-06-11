CATEGORICAL = [
    "brand",
    "model",
    "transmission",
    "fuel_type",
    "ownership",
    "spare_key",
    "reg_number",
]

NUMERICAL = [
    "car_age",
    "engine_capacity(CC)",
    "km_driven",
]

TARGET = "price"

# Production model excludes overall_cost because of possible target leakage.