from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

data = {
    "age": [22, 25, 47, 52, 46, 56, 23, 34, 42, 29,
            31, 48, 33, 26, 51, 38, 45, 27, 36, 49],    
    "income": [25000, 30000, 80000, 90000, 75000, 100000, 28000, 40000, 65000, 35000,
               45000, 85000, 48000, 32000, 95000, 60000, 70000, 37000, 52000, 88000],    
    "credit_score": [600, 650, 720, 750, 710, 780, 620, 680, 700, 660,
                     690, 730, 675, 640, 760, 705, 715, 655, 695, 740],    
    "loan_approved": [0, 0, 1, 1, 1, 1, 0, 0, 1, 0,
                      0, 1, 0, 0, 1, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)
df.head()

# train-test split
from sklearn.model_selection import train_test_split

X = df.drop("loan_approved", axis=1)
y = df["loan_approved"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# baseline
model=DecisionTreeClassifier(max_depth=1)
model.fit(X_train,y_train)
prediction=model.predict(X_test)

print("accuracy_score:",accuracy_score(y_test,prediction))
print("Train Accuracy:", model.score(X_train, y_train))
print("Test Accuracy:", model.score(X_test, y_test))
