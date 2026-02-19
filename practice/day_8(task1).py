import pandas as pd

data = {
    "age": [25, 30, 45, 35, 50, 23, 40, 60, 48, 33,
            29, 55, 37, 42, 31, 52, 27, 46, 39, 58],
    
    "monthly_bill": [200, 300, 500, 400, 600, 180, 450, 700, 520, 350,
                     250, 650, 420, 480, 310, 580, 220, 510, 390, 680],
    
    "tenure_months": [6, 12, 24, 18, 36, 4, 20, 48, 30, 15,
                      10, 40, 22, 28, 14, 35, 8, 26, 19, 45],
    
    "churn": [1, 0, 0, 0, 0, 1, 0, 0, 0, 1,
              1, 0, 0, 0, 1, 0, 1, 0, 0, 0]
}

df = pd.DataFrame(data)
df.head()

# test train split
from sklearn.model_selection import train_test_split

X=df.drop("churn",axis=1)
y=df["churn"]

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.3,random_state=42
)

# baseline
from sklearn.linear_model import LogisticRegression

model=LogisticRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

# evaluation
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
