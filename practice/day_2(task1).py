import seaborn as sns
import pandas as pd

df=sns.load_dataset('titanic')

df.head()
df.to_csv("/Users/tayyabkhan/python/practice/titanic.csv",index=True)

df.to_pickle("/Users/tayyabkhan/python/practice/data.pkl")

df.head()
df.tail()
df.shape
df.columns
df.info()
df.describe()