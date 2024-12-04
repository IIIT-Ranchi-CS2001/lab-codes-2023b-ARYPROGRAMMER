# Common
# display first 8 rows
# display last 5 rows
# display dtype and number of non null values in each column
# use numpy to compute mean AQI, max PM2.5 and min PM10 values for each city

import pandas as pd
import numpy as np

# Load AQI data
df = pd.read_csv('AQI_Data.csv')

# Display first 8 rows
print("First 8 rows:\n")
print(df.head(8))

# Display last 5 rows
print("\nLast 5 rows:\n")
print(df.tail(5))

# Display dtype and number of non null values in each column
print("\nDtype and number of non null values in each column: \n")
print(df.info())

# Compute mean AQI, max PM2.5 and min PM10 values for each city
print("\nMean AQI, max PM2.5 and min PM10 values for each city:")
print(df.groupby('City').agg({'AQI': np.mean, 'PM2.5': np.max, 'PM10': np.min}))
