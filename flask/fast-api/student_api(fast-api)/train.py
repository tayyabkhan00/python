import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

X = np.array([
    [2, 60, 40],
    [5, 80, 70],
    [1, 50, 30],
    [6, 90, 85],
    [3, 70, 50],
    [4, 75, 65]
])

y = np.array([0, 1, 0, 1, 0, 1])

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "/Users/tayyabkhan/python/flask/fast-api/student_api(fast-api)/model.pkl")

print("Model saved successfully!")
