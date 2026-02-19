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
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

model_train = model.score(X_train, y_train)
model_test = model.score(X_test, y_test)

print("Random Forest Train Accuracy:", model_train)
print("Random Forest Test Accuracy:", model_test)

# Feature Importance
import pandas as pd

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print(importance.sort_values(by="Importance", ascending=False))
