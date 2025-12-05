import numpy as np

arr = np.array([10,20,30,40,50])

mean = arr.mean()
std = arr.std()

standardized = (arr - mean) / std
print(standardized)
