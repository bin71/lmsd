import pandas as pd

# Load the dataset
file_path = r"C:\Users\rutuj\OneDrive\Desktop\DSML\IRIS.csv"
df = pd.read_csv(file_path)

# Filter the dataset for each species
species_list = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# Iterate through each species and display statistical details
for species in species_list:
    print(f"Statistics for {species}:")
    species_data = df[df['species'] == species]  # Filter data for the species
    print(species_data.describe())  # Display statistical details
    print("\n")
