import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
file_path = 'cereal.csv'
data = pd.read_csv(file_path)

# Define features and target variable
X = data.drop(columns=['rating'])
y = data['rating']

# Function to split data and print sizes
def split_and_print_sizes(X, y, test_size):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    print(f"Train-test split ratio {1-test_size}-{test_size}:")
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Testing set size: {X_test.shape[0]}\n")

# Explore different train-test split ratios
split_and_print_sizes(X, y, test_size=0.3)  # 70-30 split
split_and_print_sizes(X, y, test_size=0.2)  # 80-20 split