import pandas as pd
import numpy as np

file_path = r'Datasets\Lipstick.csv'
df = pd.read_csv(file_path)

print("Dataset:")
print(df.head())

df['Age'] = df['Age'].map({'<21': 0, '21-35': 1, '>35': 2})
df['Income'] = df['Income'].map({'Low': 0, 'Medium': 1, 'High': 2})
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Ms'] = df['Ms'].map({'Single': 0, 'Married': 1})
df['Buys'] = df['Buys'].map({'No': 0, 'Yes': 1})

print("\nEncoded Dataset:")
print(df.head())

def entropy(data):
    total = len(data)
    pos_count = np.sum(data)
    neg_count = total - pos_count
    
    if pos_count == 0 or neg_count == 0:
        return 0
    
    p_pos = pos_count / total
    p_neg = neg_count / total
    
    return -p_pos * np.log2(p_pos) - p_neg * np.log2(p_neg)

def information_gain(data, feature, target):
    unique_values = data[feature].unique()
    total_entropy = entropy(data[target])
    
    weighted_entropy = 0
    for value in unique_values:
        subset = data[data[feature] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset[target])
    
    return total_entropy - weighted_entropy

features = ['Age', 'Income', 'Gender', 'Ms']
for feature in features:
    gain = information_gain(df, feature, 'Buys')
    print(f"Information Gain for '{feature}': {gain}")

best_feature = None
max_gain = -1

for feature in features:
    gain = information_gain(df, feature, 'Buys')
    if gain > max_gain:
        max_gain = gain
        best_feature = feature

print(f"\nRoot Node of the Decision Tree: {best_feature} with Information Gain: {max_gain}")
