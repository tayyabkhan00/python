import pandas as pd

data = {
    "hours_studied": [2, 3, 5, 7, 8, 1, 4, 6, 9, 2,
                      3, 5, 6, 7, 8, 2, 4, 6, 9, 1],
    
    "attendance": [60, 65, 75, 80, 85, 55, 70, 78, 90, 62,
                   68, 74, 82, 88, 92, 58, 72, 79, 95, 50],
    
    "previous_score": [50, 55, 65, 70, 75, 45, 60, 68, 85, 52,
                       57, 66, 72, 80, 88, 48, 62, 69, 90, 40],
    
    "pass": [0, 0, 1, 1, 1, 0, 0, 1, 1, 0,
             0, 1, 1, 1, 1, 0, 0, 1, 1, 0]
}

df = pd.DataFrame(data)
df.head()

df.corr()

from sklearn.model_selection import train_test_split

X=df.drop("pass",axis=1)
y=df["pass"]

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.3,random_state=42
)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

log_reg=LogisticRegression()
log_reg.fit(X_train,y_train)

log_pred=log_reg.predict(X_test)

print(classification_report(y_test,log_pred))

from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

print("Random Forest Report:\n")
print(classification_report(y_test, rf_pred))

# Create new unseen data
new_student = pd.DataFrame({
    "hours_studied": [4],
    "attendance": [70],
    "previous_score": [60]
})

# Predict
prediction = rf_model.predict(new_student)

print("Prediction:", prediction)