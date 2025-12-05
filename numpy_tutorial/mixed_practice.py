# Create a 4×4 identity matrix.
import numpy as np

I = np.eye(4)
print(I)

# Reshape 12 elements into a 3×4 matrix.
arr = np.arange(12)
reshaped = arr.reshape(3,4)
print(reshaped)

# Max, min, mean, std
arr = np.array([4,8,2,9,5])
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.std(arr))

# Replace all values >10 with 10
arr = np.array([5,12,7,18,3,10])
arr[arr > 10] = 10
print(arr)

# Extract all even numbers from 1–20
arr = np.arange(1,21)
evens = arr[arr % 2 == 0]
print(evens)

# Stack two arrays vertically & horizontally
a = np.array([1,2,3])
b = np.array([4,5,6])
vstacked = np.vstack((a,b))
hstacked = np.hstack((a,b))
print(vstacked)
print(hstacked)

# Create a 5×5 matrix of random numbers
mat = np.random.rand(5,5)
print(mat)

# Normalize an array (0–1 range)
arr = np.array([10, 20, 30, 40])
norm = (arr - arr.min()) / (arr.max() - arr.min())
print(norm)

# Diagonal elements
mat = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

diag = np.diag(mat)
print(diag)

# Unique elements
arr = np.array([1,2,2,3,4,4,5])
unique_vals = np.unique(arr)
print(unique_vals)

# Replace negative values with 0
arr = np.array([1,-3,5,-2,9])
arr[arr < 0] = 0
print(arr)

# Dot product of two vectors
a = np.array([1,2,3])
b = np.array([4,5,6])
dot = np.dot(a,b)
print(dot)

# Flatten a 2D array
mat = np.array([[1,2],[3,4]])
flat = mat.flatten()
print(flat)

# Generate 100 random numbers (Normal dist.)
data = np.random.randn(100)
print(data)

# Sort an array
arr = np.array([4,1,7,3,9])
sorted_arr = np.sort(arr)
print(sorted_arr)

# Index of maximum value
arr = np.array([4,8,2,9,5])
idx = np.argmax(arr)
print(idx)

# Check if two arrays are equal
a = np.array([1,2,3])
b = np.array([1,2,3])
print(np.array_equal(a,b))

# Broadcasting: add 1D array to each row
mat = np.array([[1,2,3],
                [4,5,6]])
add = np.array([10,20,30])
result = mat + add
print(result)

# Convert Python list → NumPy array & multiply by 3
lst = [1,2,3,4]
arr = np.array(lst)
print(arr * 3)

# Round array values to 2 decimals
arr = np.array([1.2345, 2.3456, 3.9999])
rounded = np.round(arr, 2)
print(rounded)
