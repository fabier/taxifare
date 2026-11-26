import joblib


def load_model(model_path: str):
    """Load a trained model from the specified file path."""
    return joblib.load(filename=model_path)


def predict():
    pass
