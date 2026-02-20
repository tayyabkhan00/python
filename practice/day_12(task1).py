import pandas as pd

data = {
    "age": [25, 30, 45, 35, 50, 23, 40, 60, 48, 33,
            29, 55, 37, 42, 31, 52, 27, 46, 39, 58,
            34, 41, 26, 53, 44, 28, 36, 49, 32, 57],
    
    "monthly_bill": [200, 300, 500, 400, 600, 180, 450, 700, 520, 350,
                     250, 650, 420, 480, 310, 580, 220, 510, 390, 680,
                     360, 470, 210, 620, 490, 230, 410, 530, 340, 660],
    
    "tenure_months": [6, 12, 24, 18, 36, 4, 20, 48, 30, 15,
                      10, 40, 22, 28, 14, 35, 8, 26, 19, 45,
                      16, 25, 5, 38, 29, 7, 21, 31, 13, 42],
    
    "contract_type": ["Monthly", "Yearly", "Yearly", "Monthly", "Yearly",
                      "Monthly", "Yearly", "Yearly", "Yearly", "Monthly",
                      "Monthly", "Yearly", "Monthly", "Yearly", "Monthly",
                      "Yearly", "Monthly", "Yearly", "Monthly", "Yearly",
                      "Monthly", "Yearly", "Monthly", "Yearly", "Yearly",
                      "Monthly", "Monthly", "Yearly", "Monthly", "Yearly"],
    
    "churn": [1, 0, 0, 0, 0, 1, 0, 0, 0, 1,
              1, 0, 0, 0, 1, 0, 1, 0, 0, 0,
              1, 0, 1, 0, 0, 1, 0, 0, 1, 0]
}

df = pd.DataFrame(data)
df.head()

df.info()
df.describe()
df["contract_type"].value_counts()
df.corr(numeric_only=True)

df = pd.get_dummies(df, columns=["contract_type"], drop_first=True)

from sklearn.model_selection import train_test_split

X = df.drop("churn", axis=1)
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)

log_pred = log_model.predict(X_test)

print("Logistic Regression:\n")
print(classification_report(y_test, log_pred))

from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

print("Random Forest:\n")
print(classification_report(y_test, rf_pred))
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
})

print(importance.sort_values(by="Importance", ascending=False))
