import pandas as pd

# Load the Titanic dataset
file_path = 'Datasets\Titanic.csv'
titanic_data = pd.read_csv(file_path)

# 1. Indexing and Selecting Data
# Selecting specific columns
selected_columns = titanic_data[['Name', 'Age', 'Survived']].head()

# Setting 'PassengerId' as the index
indexed_data = titanic_data.set_index('PassengerId').head()

# 2. Sorting Data
# Sorting by 'Fare' in descending order
sorted_data = titanic_data.sort_values(by='Fare', ascending=False).head()

# 3. Describing Attributes
description = titanic_data.describe()

# 4. Checking Data Types
data_types = titanic_data.dtypes

# Display Results
print("Selected Columns:")
print(selected_columns)
print("\nIndexed Data:")
print(indexed_data)
print("\nSorted Data by 'Fare':")
print(sorted_data)
print("\nDescription of Dataset:")
print(description)
print("\nData Types of Each Column:")
print(data_types)
