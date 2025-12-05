import numpy as np

mat = np.array([
    [2, 80, 9],
    [4, 60, 7],
    [6, 70, 5]
])

min_vals = np.min(mat, axis=0)
max_vals = np.max(mat, axis=0)

scaled = (mat - min_vals) / (max_vals - min_vals)
print(scaled)


'''
This is VERY important in:
Machine learning
Deep learning
KNN
Logistic/Linear regression
Normalizing numeric data
'''