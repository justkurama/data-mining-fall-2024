import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'cereal.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print("First 5 rows of the dataframe:")
print(df.head())

# Display the last few rows of the dataframe
print("\nLast 5 rows of the dataframe:")
print(df.tail())

# Display basic information about the dataframe
print("\nDataframe info:")
print(df.info())

# Display summary statistics of the dataframe
print("\nSummary statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Display data types of each column
print("\nData types of each column:")
print(df.dtypes)
