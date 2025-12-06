from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Data
X = [[50],[60],[80],[120],[150]]
y = [0,0,1,1,1]  # 0 small, 1 big fruits

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Create model
knn = KNeighborsClassifier(n_neighbors=3)

# Train
knn.fit(X_train, y_train)

# Predict
print(knn.predict(X_test))
