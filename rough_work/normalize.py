import numpy as np

arr = np.array([10, 20, 30, 40])
norm = (arr - arr.min()) / (arr.max() - arr.min())
# print(norm)

mat = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

diag = np.diag(mat)
# print(diag)

a = np.array([1,2,3])
b = np.array([4,5,6])

dot = np.dot(a,b)
print(dot)
