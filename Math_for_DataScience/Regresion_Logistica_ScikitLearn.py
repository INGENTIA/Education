from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


atrib_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
X, y = load_iris(return_X_y=True)

clf  = LogisticRegression(random_state=10, solver='liblinear').fit(X[:100], y[:100])

print(clf.coef_)