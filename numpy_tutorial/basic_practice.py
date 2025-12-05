import numpy as np

# Create a NumPy array from 1 to 10.
arr = np.arange(1, 11)
arr

# Create an array of zeros of size 5.
arr = np.zeros(5)
arr

# Create a 2D array of shape (3,3) with all ones.
arr = np.ones((3, 3))
arr

# Create an array of even numbers between 2 and 20.
arr = np.arange(2, 21, 2)
arr

# Find the shape, size, and dimensions of this array:
arr = np.array([[1,2,3],[4,5,6]])
arr.shape   # (2, 3)
arr.size    # 6
arr.ndim    # 2

# Slice this array to get [2, 3]:
arr = np.array([1,2,3,4])
result = arr[1:3]
result

# Select element "5" from this matrix:
mat = np.array([[1,2,3],[4,5,6]])
value = mat[1, 1]
value

# Reverse this array:
arr = np.array([1,2,3,4,5])
rev = arr[::-1]
rev

# Add 10 to every element of this array:
arr = np.array([1,2,3])
result = arr + 10
result

# Multiply two arrays elementwise:
a = np.array([1,2,3])
b = np.array([4,5,6])
result = a * b
result
