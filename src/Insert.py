import pandas as pd
import numpy as np
from mysql_connection import engine

print("🚀 Script started")

df = pd.read_csv(
    "Data/feature_engineering.csv",
    parse_dates=["Order_Date"]
)

print("CSV loaded:", df.shape)

# Fix infinite values
df.replace([np.inf, -np.inf], None, inplace=True)

# Insert
df.to_sql(
    name="orders",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=1000
)

print("✅ Data inserted into MySQL successfully!")