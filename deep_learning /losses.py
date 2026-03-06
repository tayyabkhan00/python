# MSE Example:

import numpy as np

y_true = np.array([3, 3])
y_pred = np.array([4, 5])

mse = np.mean((y_pred - y_true)**2)
print(mse)

# Binary Cross Entropy Example:

y_true = np.array([1, 0, 1, 1])
y_pred = np.array([0.9, 0.1, 0.8, 0.7]) 
bce = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
print(bce)

# or

y = 1      # actual
p = 0.9    # predicted probability

bce = - (y*np.log(p) + (1-y)*np.log(1-p))
print(bce)

# Categorical Cross Entropy Example:

y_true = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
y_pred = np.array([[0.8, 0.1, 0.1], 
                   [0.2, 0.7, 0.1],
                   [0.1, 0.3, 0.6]])
cce = -np.mean(np.sum(y_true * np.log(y_pred), axis=1))
print(cce)

# or

y_true = [1, 0, 0]          # class 0 is correct
y_pred = [0.8, 0.15, 0.05]  # probabilities

cce = -np.sum(np.array(y_true) * np.log(y_pred))
print(cce)
