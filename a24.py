import pandas as pd

# Load dataset
file_path = r"C:\Users\rutuj\OneDrive\Desktop\DSML\Lipstick.csv"
df = pd.read_csv(file_path)

# Count unique values and data types
print("\nUnique values:\n", df.nunique())
print("\nData types:\n", df.dtypes)

# Convert floats with whole numbers to int, ints to str
df.update(df.select_dtypes('float64').apply(lambda x: x.astype('int64') if (x % 1).eq(0).all() else x))
df.update(df.select_dtypes('int64').astype('str'))

# Handle missing values: Fill numerical with mean, categorical with mode
df.fillna({col: df[col].mean() for col in df.select_dtypes(['float64', 'int64'])}, inplace=True)
df.fillna({col: df[col].mode()[0] for col in df.select_dtypes(['object'])}, inplace=True)

# Save cleaned data
df.to_csv(r"C:\Users\rutuj\OneDrive\Desktop\DSML\cleaned_lipstick_data.csv", index=False)
print("\nCleaned data saved successfully!")
