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



# Confusion matrix is calculated ONLY on test data.
# |          | Predicted 0 | Predicted 1 |
# | -------- | ----------- | ----------- |
# | Actual 0 | 3           | 1           |
# | Actual 1 | 0           | 2           |

# 🔹 Precision

# Question:

# Out of all customers predicted as churn, how many actually churned?

# From matrix:

# Model predicted churn = (1 + 2) = 3 people
# But actually churned = 2

# So:
# Precision = 2/3

# Meaning:
# When model says "customer will churn", it's correct 67% of the time.

# 🔹 Recall

# Question:

# Out of all actual churn customers, how many did we catch?

# Actual churn customers = (0 + 2) = 2
# Model caught = 2

# So:
# Recall = 2/2 = 1.0

# Meaning:
# Model caught ALL churn customers.

# 🔹 F1 Score

# F1 is balance between precision and recall.

# If:

# Precision high

# Recall high

# Then F1 high.

# If one low → F1 drops.

# It’s just a balanced score.

# 🔹 Support

# Support means:
# How many actual samples of that class exist.

# From matrix:

# Class 0 support = 4 (3+1)

# Class 1 support = 2 (0+2)

# So support tells how many true examples exist.