import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv("/Users/tayyabkhan/python/practice/employee.csv")


df['salary'].mean()
df['salary'].median()
df['salary'].skew()

x=df['salary']
plt.hist(x)

df['salary'].describe()
# -------------------------------------------------------
# ----------------Is 500,000 an Outlier?-----------------
# -------------------------------------------------------
# Using IQR:

# Q1 = 49,500
# Q3 = 112,500

# IQR = 112,500 − 49,500 = 63,000

# Upper limit = Q3 + 1.5 × IQR
# = 112,500 + (1.5 × 63,000)
# = 112,500 + 94,500
# = 207,000

# Anything above 207,000 is an outlier.

# Your max = 500,000

# So yes.

# It is a clear statistical outlier.
# -------------------------------------------------------
# -------------------------------------------------------
upper_limit = 207000
df['salary_capped'] = np.where(df['salary'] > upper_limit,upper_limit,df['salary'])                
df.head()

df.corr(numeric_only=True)