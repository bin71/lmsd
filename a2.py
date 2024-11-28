import pandas as pd


file_path = 'Datasets\Telecom Churn.csv'
data = pd.read_csv(file_path)

print("Dataset Overview:")
print(data.head())

print("\nSummary Statistics:")
print(data.describe())

print("\nMinimum values for each column:")
print(data.min(numeric_only=True))

print("\nMaximum values for each column:")
print(data.max(numeric_only=True))

print("\nMean values for each column:")
print(data.mean(numeric_only=True))

numeric_data = data.select_dtypes(include=['number']) 
range_values = numeric_data.max() - numeric_data.min()
print("\nRange (Max - Min) for each column:")
print(range_values)

print("\nStandard deviation for each column:")
print(data.std(numeric_only=True))

print("\nVariance for each column:")
print(data.var(numeric_only=True))


percentiles = [0.25, 0.5, 0.75] 
numeric_data = data.select_dtypes(include=['number'])  
print("\nPercentiles (25th, 50th, 75th) for each numeric column:")
print(numeric_data.quantile(percentiles))
