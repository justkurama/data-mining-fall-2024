import pandas as pd

# Load the dataset
file_path = 'cereal.csv'
cereal_df = pd.read_csv(file_path)

# Create new features
# Example: Interaction term between protein and fiber
cereal_df['protein_fiber_interaction'] = cereal_df['protein'] * cereal_df['fiber']

# Example: Polynomial feature of sugars
cereal_df['sugars_squared'] = cereal_df['sugars'] ** 2

# Example: Ratio of carbohydrates to protein
cereal_df['carbo_protein_ratio'] = cereal_df['carbo'] / (cereal_df['protein'] + 1e-5)  # Adding a small value to avoid division by zero

# Example: Total macronutrients (protein + fat + carbo)
cereal_df['total_macronutrients'] = cereal_df['protein'] + cereal_df['fat'] + cereal_df['carbo']

# Save the modified dataset to a new CSV file
output_file_path = 'cereal_modified.csv'
cereal_df.to_csv(output_file_path, index=False)

print("New features created and saved to", output_file_path)