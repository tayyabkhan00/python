# ⭐ Task 1: Handle Missing Values
import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])

# 1. Mask non-nan values
valid_vals = arr[~np.isnan(arr)]

# 2. Calculate mean
mean_val = np.mean(valid_vals)

# 3. Replace nan
arr_filled = np.where(np.isnan(arr), mean_val, arr)

print(arr_filled)

# ⭐ Task 2: Standardize the Data
data = np.array([10, 20, 30, 40, 50])
mean = np.mean(data)
std_dev = np.std(data)
z=(data - mean) / std_dev
print(z)

# ⭐ Task 3: Min-Max Scale Each Column
mat = np.array([[2,80,9],
                [4,60,7],
                [6,70,5]])

min_vals = np.min(mat, axis=0)
max_vals = np.max(mat, axis=0)

scaled = (mat - min_vals) / (max_vals - min_vals)
print(scaled)

# ⭐ Task 4: One-Hot Encoding
genders = np.array(["M","F","F","M","M"])

unique_vals = np.unique(genders)
one_hot = (genders[:, None] == unique_vals).astype(int)

print(one_hot)
