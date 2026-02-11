import pandas as pd

data = {
    "name": ["Aman", "Riya", "Aman", "John", "Riya"],
    "age": [23, 25, 23, None, 25],
    "salary": [50000, 60000, 52000, 58000, None],
    "city": ["Delhi", "Mumbai", "Delhi", "Bangalore", "Mumbai"]
}

df = pd.DataFrame(data)

# 1. Find missing values
# 2. Fill missing age with mean

# 3. Fill missing salary with median
# 4. Find average salary per city
# 5. Find how many times each name appears


# 1.----------------------------------------
df.isna().sum()

# 2.----------------------------------------
df['age']=df['age'].fillna(df['age'].mean())

# 3.----------------------------------------
df['salary']=(df['salary'].fillna(df["salary"]).median())

# 4.----------------------------------------
df.groupby('city')['salary'].mean()

# 5.----------------------------------------
df['name'].value_counts()