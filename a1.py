import pandas as pd

file_path = r'Datasets\Titanic.csv'
data = pd.read_csv(file_path)


print("First 5 rows:")
print(data.head())


print("\nSelecting the first 3 rows and specific columns (Name, Age):")
print(data.loc[0:2, ['Name', 'Age']])  


data.set_index('Name', inplace=True)
print(data.loc['Kelly, Mr. James', 'Age'])
print(data.loc['Kelly, Mr. James'])

print("\n",data.iloc[0:2, 0:1])
print(data.iloc[0])
print(data[['Survived','Age']])
print(data['Age'])



sorted_data = data.sort_values(by='Age', ascending=True)
print("\nData sorted by Age:")
print(sorted_data.head())


print("\nStatistical Summary:")
print(data.describe())


print("\nData Types of Columns:")
print(data.dtypes)
