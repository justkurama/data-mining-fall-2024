import pandas as pd
import numpy as np

# Sample dataset
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, np.nan, np.nan, 4, 5]
}

df = pd.DataFrame(data)

# Identify missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Remove rows with missing values
df_dropna = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropna)

# Fill missing values with the mean
df_fillna_mean = df.fillna(df.mean())
print("\nDataFrame after filling missing values with the mean:")
print(df_fillna_mean)

# Fill missing values with the median
df_fillna_median = df.fillna(df.median())
print("\nDataFrame after filling missing values with the median:")
print(df_fillna_median)

# Fill missing values with a specific value (e.g., 0)
df_fillna_value = df.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_fillna_value)

# Forward fill (ffill)
df_ffill = df.ffill()
print("\nDataFrame after forward filling missing values:")
print(df_ffill)

# Backward fill (bfill)
df_bfill = df.bfill()
print("\nDataFrame after backward filling missing values:")
print(df_bfill)