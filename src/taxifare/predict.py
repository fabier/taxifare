import joblib
import numpy as np
import pandas as pd


def load_model(model_path: str):
    """Load a trained model from the specified file path."""
    return joblib.load(filename=model_path)


def predict(model, data):
    """Make predictions using the loaded model and input data."""
    return model.predict(data)


def __sample_data(num_rows=5):
    """Generates **num_rows** of random data"""
    start_date = pd.to_datetime("2011-01-01")
    random_days = np.random.randint(0, 5 * 365 + 1, size=num_rows)
    dates = pd.to_timedelta(random_days, unit="D") + start_date

    return pd.DataFrame(
        {
            "pickup_datetime": dates,
            "pickup_longitude": np.random.normal(
                loc=-73.975, scale=0.0338, size=num_rows
            ),
            "pickup_latitude": np.random.normal(
                loc=40.750, scale=0.0266, size=num_rows
            ),
            "dropoff_longitude": np.random.normal(
                loc=-73.974, scale=0.0338, size=num_rows
            ),
            "dropoff_latitude": np.random.normal(
                loc=40.751, scale=0.0305, size=num_rows
            ),
            "passenger_count": np.random.randint(low=1, high=6 + 1, size=num_rows),
        }
    )


if __name__ == "__main__":
    model = load_model("models/linreg_pipeline.joblib")
    print("Model loaded : OK")
    data = __sample_data()
    print(f"\nInput data :\n=====\n{data}\n")
    predictions = predict(model=model, data=data)
    print(f"\nPredictions :\n=====\n{predictions}")
