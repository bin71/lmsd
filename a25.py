import pandas as pd

# Step 1: Load the dataset
# Correct the file path by using a raw string or escaping backslashes
file_path = r"C:\Users\rutuj\OneDrive\Desktop\DSML\cleaned_sample_data.csv"  # Use raw string
# Alternatively:
# file_path = "C:\\Users\\rutuj\\Downloads\\Datasets\\Datasets\\Lipstick.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Step 2: Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 3: Display basic info about the dataset
print("\nDataset Info:")
print(df.info())

# Step 4: Handle missing values
# Fill missing numerical values with the column mean
numerical_cols = df.select_dtypes(include=["float64", "int64"]).columns
df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

# Fill missing categorical values with the most frequent value
categorical_cols = df.select_dtypes(include=["object"]).columns
df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])

# Step 5: Remove duplicates
df = df.drop_duplicates()

# Step 6: Rename columns for clarity
df.rename(columns=lambda x: x.strip().replace(" ", "_").lower(), inplace=True)

# Step 7: Save cleaned data to a new CSV file
cleaned_file_path = "cleaned_sample_data.csv"
df.to_csv(cleaned_file_path, index=False)

# Final Output
print("\nCleaned Dataset:")
print(df.head())
print(f"\nCleaned dataset saved to {cleaned_file_path}")
