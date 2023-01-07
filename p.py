import pandas as pd
print(pd.__version__)

datacolumn = {'day1': 420, 'day2': 380}
series = pd.Series(datacolumn)
print(series)

dataset = {
    'names': ['a', 'b', 'c'],
    'ages': [1, 2, 3],
    'math': [8, 9, 8]
}
df = pd.DataFrame(dataset)
print(df)
print(df.loc[2])
print(df.loc[[0, 1]])

df = pd.read_json('data.json')
print(df)

df = pd.read_csv('data.csv')
print(df)
print(df.to_string())
print(df.head(10))
print(df.tail(10))
print(df["Calories"].mean())
print(df["Calories"].median())
print(df["Calories"].mode())   #return dataframe
print(df.info())

new_df = df.dropna()
print(new_df.info())

df['Calories'].fillna(df["Calories"].mode()[0], inplace = True)
print(df.info())

for x in df.index:
    if (df.loc[x, "Duration"] >= 120):
        df.drop(x, inplace = True)
print(df.info())

print(df.duplicated().head(20))
df.drop_duplicates(inplace = True)
print(df.duplicated().head(20))

print(df.corr())

import matplotlib.pyplot as plt
df.plot()
plt.show()