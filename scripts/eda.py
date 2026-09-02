
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@localhost:5432/mydb")
engine = create_engine(DATABASE_URL)

def perform_eda():
    df = pd.read_sql("SELECT * FROM sales", engine)
    print(df.head())
    print(df.info())
    print(df.describe())

    # Выручка по категориям
    df['revenue'] = df['quantity'] * df['price']
    category_revenue = df.groupby('category')['revenue'].sum().sort_values(ascending=False)
    print(category_revenue)
    # График топ товаров
    os.makedirs('reports', exist_ok=True)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=category_revenue.index, y=category_revenue.values)
    plt.title("Выручка по категориям")
    plt.savefig("reports/category_revenue.png")
    plt.show()
    plt.close()

if __name__ == "__main__":
    perform_eda()