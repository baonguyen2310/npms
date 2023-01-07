import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

arr = np.array([0, 1, 2, 3, 4, 5])
sns.distplot(arr)
plt.show()

df = pd.read_csv("data.csv")

df = sns.load_dataset("penguins")
sns.pairplot(df, hue = "species")
plt.show()