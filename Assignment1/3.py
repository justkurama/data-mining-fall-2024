import pandas as pd
from sklearn.preprocessing import MinMaxScaler
# Load the dataset
df = pd.read_csv('cereal.csv')

# Normalize numerical features using Min-Max scaling
numerical_features = ['calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins', 'weight', 'cups', 'rating']
min_max_scaler = MinMaxScaler()
df[numerical_features] = min_max_scaler.fit_transform(df[numerical_features])

# Encode categorical variables using one-hot encoding
categorical_features = ['mfr', 'type']
df = pd.get_dummies(df, columns=categorical_features)

# Bin continuous variables into discrete intervals
df['calories_binned'] = pd.cut(df['calories'], bins=5, labels=False)
df['sodium_binned'] = pd.cut(df['sodium'], bins=5, labels=False)

# Display the transformed dataframe
print(df.head())