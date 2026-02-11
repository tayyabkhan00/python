import pandas as pd

df = pd.read_csv("/Users/tayyabkhan/python/practice/titanic.csv")

# ---------------------------------------------------------------
# Calculates the percentage of missing values in each column.
(df.isnull().sum() / len(df)) * 100

# ---------------------------------------------------------------
# drop the unnecessary column
df.drop(columns=["deck"],inplace=True)

# ---------------------------------------------------------------
# duplicate value
df.duplicated().sum()

# ---------------------------------------------------------------
# Converting String Numbers → Numeric
df["sex"] = df["sex"].map({"male": 0, "female": 1})
df["sex"].head(2)

# ---------------------------------------------------------------
# Top Categories by Count
df['embark_town'].value_counts().head(3)

# ---------------------------------------------------------------
# average age by city
# Survival by Passenger Class
# Median Age by Class
# Survival Rate by Gender
print(df.groupby('embark_town')['age'].mean())
print(df.groupby("pclass")["survived"].mean())
print(df.groupby("sex")["survived"].mean())
print(df.groupby("pclass")["age"].median())

