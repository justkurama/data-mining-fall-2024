import pandas as pd
from scipy import stats

# Load the data
file_path = 'cereal.csv'
df = pd.read_csv(file_path)

# Step 1: Remove duplicate rows
df = df.drop_duplicates()

# Step 2: Detect and remove outliers using the Z-score method
z_scores = stats.zscore(df.select_dtypes(include=['float64', 'int64']))
abs_z_scores = abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
df = df[filtered_entries]

# Step 3: Correct inconsistencies in categorical data
# Example: Standardizing manufacturer names
df['mfr'] = df['mfr'].str.upper()

# Save the cleaned data to a new CSV file
cleaned_file_path = 'cleaned_cereal.csv'
df.to_csv(cleaned_file_path, index=False)

print("Data cleaning complete. Cleaned data saved to:", cleaned_file_path)