import pandas as pd

df = pd.read_csv("cars.csv").iloc[:100]

df.to_sql("cars", "postgresql://postgres:postgres@localhost:5432/cars", index=True)
