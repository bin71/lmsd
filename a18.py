import pandas as pd

# Load the dataset
file_path = r"C:\Users\rutuj\OneDrive\Desktop\DSML\House Data.csv"
df = pd.read_csv(file_path)

# Display the first few rows to understand the structure of the data
print("Dataset Preview:")
print(df.head())

# Define categorical and quantitative variables
# Replace 'Age_Group' and 'Income' with actual column names from your dataset
categorical_variable = 'Age_Group'  # Example categorical variable
quantitative_variable = 'Income'  # Example quantitative variable

# Ensure the columns exist in the dataset
if categorical_variable in df.columns and quantitative_variable in df.columns:
    # Group by the categorical variable and calculate summary statistics
    grouped_stats = df.groupby(categorical_variable)[quantitative_variable].agg(['mean', 'median', 'min', 'max', 'std'])

    print(f"\nSummary statistics of {quantitative_variable} grouped by {categorical_variable}:")
    print(grouped_stats)
else:
    print(f"Error: Column names {categorical_variable} or {quantitative_variable} not found in the dataset.")


