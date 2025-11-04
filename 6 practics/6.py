import pandas as pd      
df = pd.read_parquet("titanic.parquet")
df.to_csv('titanic.csv')