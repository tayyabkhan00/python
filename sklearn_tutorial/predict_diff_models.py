from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Dataset
X = [[50], [60], [80], [120], [150]]
y = [0, 0, 1, 1, 1]   # 0 = small, 1 = big

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Test sample
sample = [[100]]

# ----------- MODELS ------------
knn = KNeighborsClassifier(n_neighbors=3)
tree = DecisionTreeClassifier()
logreg = LogisticRegression()
svm = SVC()

# ----------- TRAIN MODELS ------------
knn.fit(X_train, y_train)
tree.fit(X_train, y_train)
logreg.fit(X_train, y_train)
svm.fit(X_train, y_train)

# ----------- PREDICT ------------
print("KNN prediction:", knn.predict(sample))
print("Decision Tree prediction:", tree.predict(sample))
print("Logistic Regression prediction:", logreg.predict(sample))
print("SVM prediction:", svm.predict(sample))
