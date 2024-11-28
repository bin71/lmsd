import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\rutuj\OneDrive\Desktop\DSML\Titanic.csv"
df = pd.read_csv(file_path)

# Check if 'fare' column exists
if 'fare' in df.columns:
    # Plot the histogram of 'fare'
    plt.figure(figsize=(10, 6))
    plt.hist(df['fare'].dropna(), bins=30, color='skyblue', edgecolor='black')
    plt.title('Distribution of Ticket Fare on Titanic', fontsize=16)
    plt.xlabel('Fare', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.grid(axis='y', alpha=0.75)
    plt.show()
else:
    print("'fare' column not found in the dataset.")
