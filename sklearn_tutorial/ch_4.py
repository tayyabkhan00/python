from sklearn.preprocessing import StandardScaler

X = [[1],[5],[10]]

scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)

print("Before:", X)
print("After:", scaled_X)


# Use fit_transform on training data
# Use transform on test data only