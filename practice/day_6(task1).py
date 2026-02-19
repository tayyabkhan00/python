from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X=[[25],[46],[34],[33],[67],[78],[89],[86]]
y=[0,1,1,1,0,0,1,1]

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

model=DecisionTreeClassifier(max_depth=1)
model.fit(X_train,y_train)
prediction=model.predict(X_test)

print("accuracy_score:",accuracy_score(y_test,prediction))
print("Train Accuracy:", model.score(X_train, y_train))
print("Test Accuracy:", model.score(X_test, y_test))
