# generate the dataset

import pandas as pd
import numpy as np

np.random.seed(42)

n = 300

data = {
    "area": np.random.normal(1500, 400, n),              # square feet
    "bedrooms": np.random.randint(1, 6, n),
    "bathrooms": np.random.randint(1, 4, n),
    "age": np.random.randint(0, 30, n),
    "distance_to_city": np.random.normal(10, 5, n),      # km
    # np.random.normal(mean, standard_deviation, number_of_values)
}

df = pd.DataFrame(data)

# Create price with noise (so model is realistic)
df["price"] = (
    df["area"] * 150
    + df["bedrooms"] * 10000
    + df["bathrooms"] * 8000
    - df["age"] * 2000
    - df["distance_to_city"] * 3000
    + np.random.normal(0, 20000, n)
)

# split data
from sklearn.model_selection import train_test_split

X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# scaling as Regularization requires scaling.
# ⚠️ If you skip scaling → your Ridge/Lasso results will be wrong.
from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

# linear regression baseline 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

model=LinearRegression()
model.fit(X_train_scaled,y_train)
lr_predict=model.predict(X_test_scaled)

print("r2 socre:", r2_score(y_test,lr_predict))

# Ridge
from sklearn.linear_model import Ridge

ridge = Ridge(alpha=10)
ridge.fit(X_train_scaled, y_train)

ridge_pred = ridge.predict(X_test_scaled)

print("Ridge R2:", r2_score(y_test, ridge_pred))

# Lasso
from sklearn.linear_model import Lasso

lasso = Lasso(alpha=500)
lasso.fit(X_train_scaled, y_train)

lasso_pred = lasso.predict(X_test_scaled)

print("Lasso R2:", r2_score(y_test, lasso_pred))

# cross-validation
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

pipeline = make_pipeline(StandardScaler(), Ridge(alpha=10))

cv_scores = cross_val_score(
    pipeline,
    X,
    y,
    cv=5,
    scoring="r2"
)

print("CV Scores:", cv_scores)
print("Average CV R2:", cv_scores.mean())

