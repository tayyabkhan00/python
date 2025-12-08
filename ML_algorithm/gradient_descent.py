import numpy as np

# Data (example: hours studied vs marks)
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([40, 50, 60, 70, 80], dtype=float)

# Step 1: Initialize parameters
m = 0      # slope
b = 0      # intercept

# Hyperparameters
learning_rate = 0.01
epochs = 1000   # iterations

n = len(X)

# Step 2: Gradient Descent Loop
for i in range(epochs):
    y_pred = m * X + b   # prediction line
    
    # Step 3: Calculate gradients
    dm = (-2/n) * sum(X * (y - y_pred))
    db = (-2/n) * sum(y - y_pred)
    
    # Step 4: Update m and b
    m = m - learning_rate * dm
    b = b - learning_rate * db
    
    # Optional: print every 100 steps
    if i % 100 == 0:
        loss = np.mean((y - y_pred) ** 2)
        print(f"Epoch {i}, Loss = {loss:.4f}")

# Final values
print("\nFinal slope (m):", m)
print("Final intercept (b):", b)
print("Prediction for 7 hours:", m * 7 + b)
