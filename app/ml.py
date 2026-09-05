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
        with open(FEATURES_PATH, 'r') as f:
            features_list = [line.strip() for line in f if line.strip()]
    return model, scaler, features_list


def prepare_features(input_data: dict):
    """
    input_data: dict с ключами:
    - date: str (YYYY-MM-DD)
    - category: str
    - region: str
    - product_name: str
    - price: float
    """
    df = pd.DataFrame([input_data])
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['dayofweek'] = df['date'].dt.dayofweek

    df = pd.get_dummies(df, columns=['category', 'region', 'product_name'], drop_first=True)

    # Добавляем недостающие колонки (нулевые) и упорядочиваем по features_list
    model, scaler, features_list = load_model()
    for col in features_list:
        if col not in df.columns:
            df[col] = 0
    df = df[features_list]
    return df

def predict_sales(data: dict):
    """
    Возвращает предсказанное количество продаж.
    """
    model, scaler, _ = load_model()
    df = prepare_features(data)
    X = scaler.transform(df)
    prediction = model.predict(X)
    return float(prediction[0])


def load_features_list():
    path = os.path.join(os.path.dirname(__file__), 'ml_models', 'features_list.txt')
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]