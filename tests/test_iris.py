import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/iris.csv")

def test_data_exists():
    assert DATA_PATH.exists(), f"{DATA_PATH} does not exist"

def test_data_not_empty():
    df = pd.read_csv(DATA_PATH)
    assert not df.empty, "CSV file is empty"

def test_columns_exist():
    df = pd.read_csv(DATA_PATH)
    expected_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
    for col in expected_columns:
        assert col in df.columns, f"Missing column: {col}"
