import pandas as pd
import numpy as np

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
df.groupby('embark_town')['age'].mean()
df.groupby("pclass")["survived"].mean()
df.groupby("sex")["survived"].mean()
df.groupby("pclass")["age"].median()


# detect outliers in Age or Fare (Fare is better).
Q1 = df["fare"].quantile(0.25)
Q3 = df["fare"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["fare"] < lower_bound) | (df["fare"] > upper_bound)]

len(outliers)

df["Fare_log"] = np.log1p(df["fare"])
