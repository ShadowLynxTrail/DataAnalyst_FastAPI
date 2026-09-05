import joblib
import pandas as pd
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'ml_models', 'sales_model.pkl')
SCALER_PATH = os.path.join(os.path.dirname(__file__), 'ml_models', 'scaler.pkl')
FEATURES_PATH = os.path.join(os.path.dirname(__file__), 'ml_models', 'features_list.txt')

model = None
scaler = None
features_list = None

def load_model():
    global model, scaler, features_list
    if model is None:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        with open(FEATURES_PATH, 'r', encoding='utf-8') as f:
            features_list = [line.strip() for line in f if line.strip()]
    return model, scaler, features_list


def prepare_features(input_data: dict):
    model, scaler, features_list = load_model()
    df = pd.DataFrame(0, index=[0], columns=features_list)

    date = pd.to_datetime(input_data['date'])
    df['year'] = date.year
    df['month'] = date.month
    df['day'] = date.day
    df['dayofweek'] = date.dayofweek
    df['price'] = input_data['price']

    category_col = f"category_{input_data['category']}"
    if category_col in df.columns:
        df[category_col] = 1
    region_col = f"region_{input_data['region']}"
    if region_col in df.columns:
        df[region_col] = 1
    product_col = f"product_name_{input_data['product_name']}"
    if product_col in df.columns:
        df[product_col] = 1

    return df

def predict_sales(data: dict):
    model, scaler, _ = load_model()
    df = prepare_features(data)
    X = scaler.transform(df)
    prediction = model.predict(X)
    return float(prediction[0])


def load_features_list():
    path = os.path.join(os.path.dirname(__file__), 'ml_models', 'features_list.txt')
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]