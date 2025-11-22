import pandas as pd
import numpy as np

# 1️⃣ Create dataset (no external file)
df = pd.DataFrame({
    "Name": ["Aman", "Riya", "John", "Sara", "Irfan", "Tina"],
    "Age": [25, 28, np.nan, 32, 29, 40],
    "Dept": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Salary": [50000, 45000, 52000, 60000, None, 70000]
})

print("Original Data:\n", df, "\n")

# 2️⃣ Check missing values
print("Missing Values:\n", df.isna().sum(), "\n")

# 3️⃣ Fill missing numeric values with mean
# df.fillna({"Age":df["Age"].mean()}, inplace=True) 
# or 
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())

# 4️⃣ Convert column types
df["Age"] = df["Age"].astype(int)

# 5️⃣ Add new column: Annual Salary
df["Annual_Salary"] = df["Salary"] * 12

# 6️⃣ Group by department: average salary
dept_avg = df.groupby("Dept")["Salary"].mean()
print("Average Salary by Department:\n", dept_avg, "\n")

# 7️⃣ Filter: employees earning > 55000
high_salary = df[df["Salary"] > 55000]
print("High Salary Employees:\n", high_salary, "\n")

# 8️⃣ Sort employees by salary
sorted_df = df.sort_values(by="Salary", ascending=False)
print("Sorted by Salary:\n", sorted_df, "\n")

# 9️⃣ Describe statistics
print("Statistics:\n", df.describe(), "\n")

# 🔟 Final cleaned DataFrame
print("Final Cleaned Data:\n", df)
