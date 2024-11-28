import pandas as pd
import numpy as np

# Create the dataset as shown in the table
data = {
    'Age': ['Young', 'Young', 'Middle', 'Old', 'Old', 'Old', 'Middle', 'Young', 'Young', 
            'Old', 'Young', 'Middle', 'Middle', 'Middle', 'Old'],
    'Income': ['High', 'High', 'High', 'Medium', 'Low', 'Low', 'Low', 'Medium', 'Low', 
               'Medium', 'Medium', 'Medium', 'High', 'High', 'Medium'],
    'Married': ['No', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 
                'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No'],
    'Health': ['Fair', 'Good', 'Fair', 'Fair', 'Fair', 'Good', 'Good', 'Fair', 'Fair', 
               'Fair', 'Good', 'Good', 'Fair', 'Fair', 'Good'],
    'Class': ['No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 
              'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

# Load the data into a DataFrame
df = pd.DataFrame(data)

# Step 1: Frequency table for Age
freq_table = df.groupby(['Age', 'Class']).size().unstack(fill_value=0)
freq_table['Total'] = freq_table.sum(axis=1)
freq_table['Proportion_No'] = freq_table['No'] / freq_table['Total']
freq_table['Proportion_Yes'] = freq_table['Yes'] / freq_table['Total']
print("Frequency Table for Age:")
print(freq_table)

# Step 2: Calculate Entropy for the dataset
def calculate_entropy(proportions):
    return -sum(p * np.log2(p) for p in proportions if p > 0)

# Calculate overall entropy
total_count = df.shape[0]
overall_counts = df['Class'].value_counts(normalize=True)
overall_entropy = calculate_entropy(overall_counts)
print(f"\nOverall Entropy: {overall_entropy:.4f}")

# Step 3: Calculate Entropy for each split on Age
entropy_age_split = {}
for age, group in df.groupby('Age'):
    count = group.shape[0]
    class_proportions = group['Class'].value_counts(normalize=True)
    entropy_age_split[age] = calculate_entropy(class_proportions)

# Step 4: Calculate Weighted Entropy
weighted_entropy = sum(
    (df[df['Age'] == age].shape[0] / total_count) * entropy
    for age, entropy in entropy_age_split.items()
)

print(f"\nWeighted Entropy after splitting on Age: {weighted_entropy:.4f}")

# Step 5: Calculate Information Gain
info_gain = overall_entropy - weighted_entropy
print(f"\nInformation Gain when splitting on Age: {info_gain:.4f}")
