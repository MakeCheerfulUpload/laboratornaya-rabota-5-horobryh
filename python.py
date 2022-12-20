import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('final_csv.csv', delimiter=';')

data.groupby('<DATE>').boxplot(figsize=(15, 10), fontsize=10)
plt.show()
