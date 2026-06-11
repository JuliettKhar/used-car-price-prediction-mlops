from data import read_data, clean_data
from features import (
    CATEGORICAL,
    NUMERICAL,
    TARGET,
)
from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score
import pickle
import os
import mlflow
import mlflow.sklearn

MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"
EXPERIMENT_NAME = "used-car-price-prediction"

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
mlflow.set_experiment(EXPERIMENT_NAME)

def train_model():
    df = read_data('data/pre-owned cars.csv')
    df_clean = clean_data(df)

    df_train = df_clean[df_clean['make_year'] <= 2021].copy()
    df_test = df_clean[df_clean['make_year'] > 2021].copy()

    train_dicts = df_train[CATEGORICAL + NUMERICAL].to_dict(orient="records")
    test_dicts = df_test[CATEGORICAL + NUMERICAL].to_dict(orient="records")

    dv = DictVectorizer()

    X_train = dv.fit_transform(train_dicts)
    X_test = dv.transform(test_dicts)

    y_train = df_train[TARGET].values
    y_test = df_test[TARGET].values

    params = {
        "n_estimators": 100,
        "max_depth": 15,
        "random_state": 42,
        "n_jobs": -1,
    }

    with mlflow.start_run():
        mlflow.set_tag("developer", "julia")
        mlflow.set_tag("model_type", "random_forest")
        mlflow.set_tag("split_type", "time_based")
        mlflow.set_tag("model_feature_included", "true")
        mlflow.set_tag("leakage_features_excluded", "overall_cost")
        
        mlflow.log_param("train_condition", "make_year <= 2021")
        mlflow.log_param("test_condition", "make_year > 2021")
        mlflow.log_param("categorical_features", CATEGORICAL)
        mlflow.log_param("numerical_features", NUMERICAL)
        mlflow.log_params(params)

        model = RandomForestRegressor(**params)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        rmse = root_mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("r2", r2)

        os.makedirs("models", exist_ok=True)

        with open('models/dv.pkl', "wb") as f_out:
            pickle.dump(dv, f_out)

        with open("models/model.pkl", "wb") as f_out:
            pickle.dump(model, f_out)

        mlflow.log_artifact("models/dv.pkl", artifact_path="preprocessor")
        mlflow.log_artifact("models/model.pkl", artifact_path="model")
        model_info = mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model"
        )

        mlflow.register_model(
            model_info.model_uri,
            "used-car-price-model"
        )

        print("RMSE:", rmse)
        print("MAE:", mae)
        print("R²:", r2)



if __name__ == "__main__":
    train_model()