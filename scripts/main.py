# import subprocess
# import sys

from generate_data import generate
from eda import perform_eda

# def main():
#     print("Генерация данных...")
#     subprocess.run([sys.executable, "scripts/generate_data.py"], check=True)
#     print("Анализ данных...")
#     subprocess.run([sys.executable, "scripts/eda.py"], check=True)

if __name__ == "__main__":
        generate()
        perform_eda()