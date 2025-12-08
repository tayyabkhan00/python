from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [[22], [25], [47], [52], [46], [56]]     # age
y = [0, 0, 1, 1, 1, 1]                       # buys product? yes/no

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([[30]]))
print(model.predict([[50]]))

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))
plot_tree(model, filled=True)
plt.show()
