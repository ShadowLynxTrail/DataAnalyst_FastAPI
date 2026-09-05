import pandas as pd
from sqlalchemy import create_engine
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@localhost:5432/mydb")
engine = create_engine(DATABASE_URL)


def load_data():
    df = pd.read_sql("SELECT * FROM sales", engine)
    return df

def train_model():
    df = load_data()
    print(f"Загружено {len(df)} записей")

    # Преобразуем дату в числовые признаки (год, месяц, день)
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['dayofweek'] = df['date'].dt.dayofweek

    # Кодируем категориальные признаки (category, region, product_name)
    df = pd.get_dummies(df, columns=['category', 'region', 'product_name'], drop_first=True)

    # Определяем признаки и целевую переменную
    target = 'quantity'
    features = [col for col in df.columns if col not in ['id', 'date', 'quantity', 'customer']]

    X = df[features]
    y = df[target]

    # Разделяем данные
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Масштабируем признаки
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Обучаем модель (Random Forest)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Оцениваем модель
    y_pred = model.predict(X_test_scaled)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"MAE: {mae:.2f}")
    print(f"R2: {r2:.2f}")

    # Сохраняем модель и скейлер
    os.makedirs('app/ml_models', exist_ok=True)
    joblib.dump(model, 'app/ml_models/sales_model.pkl')
    joblib.dump(scaler, 'app/ml_models/scaler.pkl')
    print("Модель сохранена в app/ml_models/")

    features_list = list(X.columns)

    # Сохраняем features_list
    with open('app/ml_models/features_list.txt', 'w', encoding='utf-8') as f:
        for feature in features_list:
            f.write(feature + '\n')

if __name__ == "__main__":
    train_model()