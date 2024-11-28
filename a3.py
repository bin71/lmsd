import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = r'Datasets\House Data.csv'
data = pd.read_csv(file_path)

columns = data.columns[1:]

for column in columns:
        data[column] = data[column].replace({r'\$': '', ',': ''}, regex=True)
        data[column] = pd.to_numeric(data[column], errors='coerce')
        if data[column].isna().sum() > 0:
            if data[column].dtype == 'object':
                data[column] = data[column].fillna(data[column].mode()[0])
            else:
                data[column] = data[column].fillna(data[column].mean())

for column in columns:
    
    if pd.api.types.is_numeric_dtype(data[column]) and not data[column].isna().all():
        print(f"--- {column} ---")
        print(f"Standard Deviation: {data[column].std():.2f}")
        print(f"Variance: {data[column].var():.2f}")
        print(f"25th Percentile: {data[column].quantile(0.25):.2f}")
        print(f"50th Percentile (Median): {data[column].quantile(0.50):.2f}")
        print(f"75th Percentile: {data[column].quantile(0.75):.2f}")
        print()

for column in columns:
    if pd.api.types.is_numeric_dtype(data[column]) and not data[column].isna().all():
        plt.figure(figsize=(8, 6))
        plt.hist(data[column], bins=20, color='skyblue', edgecolor='black')
        plt.title(f"Histogram of {column}")
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

print(data[['BuildingAge', 'NumberOfBathrooms', 'NumberFloorsofBuilding', 'NumberOfBalconies', 'NumberOfWCs']])
