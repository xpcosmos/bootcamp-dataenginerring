import os
import pandas as pd

pd.read_csv('taxi_zone_lookup.csv', nrows=10)
df = pd.read_csv('green_tripdata_2019-10.csv', nrows=10)

print(pd.io.sql.get_schema(df, name='green_tripdata_2019'))