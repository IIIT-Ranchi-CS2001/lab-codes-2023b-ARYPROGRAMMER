# SET -4
# USING pivot table summarize the dataset where :
# a. The rows represent the unique city
# b. The values in the table should be maximum PM2.5 recorded for each city
# Display the resulting pivot table and save it in a pivot.csv file. If the file already exists, overwrite it otherwise create a new file.

import pandas as pd
import numpy as np

# Load AQI data
df = pd.read_csv('AQI_Data.csv')

pivot_table = pd.pivot_table(df, values='PM2.5', index='City', aggfunc=np.max)
print("\nPivot table:")
print(pivot_table)

pivot_table.to_csv('pivot.csv', index=True)
print("\nSaved pivot table to pivot.csv")

