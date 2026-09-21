import pandas as pd

def load_data():
    # Placeholder ingestion (could be replaced with file/DB ingestion)
    data = pd.DataFrame({
        "feature1": [1, 2, 3, 4, 5],
        "feature2": [100, 200, 300, 400, 500],
        "target": [10, 20, 30, 40, 50],
    })
    return data

if __name__ == "__main__":
    df = load_data()
    print(df.head())
