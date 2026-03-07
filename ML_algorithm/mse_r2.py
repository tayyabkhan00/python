from sklearn.metrics import mean_squared_error, r2_score

y_true = [60, 70, 80]
y_pred = [57, 69, 78]

print("MSE:", mean_squared_error(y_true, y_pred))
print("R2 Score:", r2_score(y_true, y_pred))



# MSE = How wrong are predictions?
# Lower = better
# R² = How good is the line?
# Higher = better
# Yes, R² can be negative. It happens when the model performs worse than simply predicting the mean of the target variable.