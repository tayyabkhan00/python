import pandas as pd

data = {
    "area_sqft": [800, 1000, 1200, 1500, 1800, 900, 1100, 1400, 1700, 2000,
                  850, 1050, 1250, 1600, 1900, 950, 1150, 1450, 1750, 2100],
    
    "bedrooms": [2, 2, 3, 3, 4, 2, 3, 3, 4, 5,
                 2, 3, 3, 4, 4, 2, 3, 4, 4, 5],
    
    "age_years": [10, 8, 6, 5, 3, 12, 7, 6, 4, 2,
                  11, 9, 7, 5, 3, 13, 8, 6, 4, 1],
    
    "price_lakhs": [40, 50, 65, 80, 95, 45, 60, 75, 90, 110,
                    42, 55, 68, 85, 100, 48, 62, 78, 92, 115]
}

df = pd.DataFrame(data)
df.head()

df["price_per_sqft"] = df["price_lakhs"] / df["area_sqft"]
df["bedroom_density"] = df["bedrooms"] / df["area_sqft"]
df["is_new"] = df["age_years"].apply(lambda x: 1 if x <= 5 else 0)

df.head()

from sklearn.model_selection import train_test_split

X = df.drop(["price_lakhs", "price_per_sqft"], axis=1)
y = df["price_lakhs"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

lr = LinearRegression()
lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)


print("Linear Regression R2:", r2_score(y_test, lr_pred))
print("MAE:", mean_absolute_error(y_test, lr_pred))

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print("Random Forest R2:", r2_score(y_test, rf_pred))
print("MAE:", mean_absolute_error(y_test, rf_pred))

print("Train R2:", rf.score(X_train, y_train))
print("Test R2:", rf.score(X_test, y_test))

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf.feature_importances_
})

print(importance.sort_values(by="Importance", ascending=False))

