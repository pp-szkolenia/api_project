import pandas as pd

table = pd.read_csv('cars.csv')

print(table.head())

table.iloc[:100].to_sql('cars','postgresql://postgres:postgres@localhost:5432/cars',index=False , if_exists='replace')

print(table.dtypes)

