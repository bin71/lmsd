import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/content/IRIS.csv')

print(data.head())

for col in data.columns[:-1]:
  plt.figure(figsize = (8,6))
  plt.boxplot(data[col], patch_artist = True, notch = True, boxprops = dict(facecolor = 'pink', color = 'red'))
  plt.ylabel('Values')
  plt.xlabel(col)
  plt.title(f'Box Plot of {col}')
  plt.show()

print('Outliers')  
for col in data.columns[:-1]:
  Q1 = data[col].quantile(0.25)
  Q3 = data[col].quantile(0.75)

  IQR = Q3 - Q1

  lower_bound = Q1 - 1.5 * IQR
  upper_bound = Q3 + 1.5 * IQR

  outliers = data[(data[col] < lower_bound)| (data[col] > upper_bound)]
  print(f"Outliers in {col}:")
  if len(outliers) > 0:  
    print(len(outliers))  
    print(outliers[col].values)
  else:
    print('0')   

