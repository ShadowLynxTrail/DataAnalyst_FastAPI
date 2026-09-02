
# импорты
import random
import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import func
import pandas as pd
import os
from dotenv import load_dotenv

os.makedirs('reports', exist_ok=True)


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@localhost:5432/mydb")
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    product_name = Column(String)
    category = Column(String)
    region = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    customer = Column(String)  # например, "Больница №1", "ВетКлиника"

def generate():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    db = Session()
    # удаляем дубликаты
    db.query(Sale).delete()
    db.commit()
    # Генерируем  записи
    products = [
        ("Тест-система COVID-19", "Лабораторная диагностика", 1200),
        ("Реагент для гематологии", "Лабораторная диагностика", 800),
        ("Шприцы 5 мл", "Расходные материалы", 15),
        ("Перчатки нитриловые", "Расходные материалы", 50),
        ("Катетеры", "Расходные материалы", 200),
        ("Набор для ветеринарии", "Ветеринария", 1500),
        ("Анализатор глюкозы", "Диагностическое оборудование", 25000),
    ]
    regions = ["Москва", "Санкт-Петербург", "Казань", "Новосибирск", "Екатеринбург"]
    customers = ["Больница №1", "Больница №2", "ВетКлиника А", "ВетКлиника Б", "Поликлиника №3"]

    sales = []
    for _ in range(10000):
        product = random.choice(products)
        date = datetime.date(2023, 1, 1) + datetime.timedelta(days=random.randint(0, 365))
        sales.append(Sale(
            date=date,
            product_name=product[0],
            category=product[1],
            region=random.choice(regions),
            quantity=random.randint(1, 50),
            price=product[2] * random.uniform(0.8, 1.2),
            customer=random.choice(customers)
        ))
    db.add_all(sales)
    db.commit()
    print("Данные успешно сгенерированы!")

if __name__ == "__main__":
    generate()