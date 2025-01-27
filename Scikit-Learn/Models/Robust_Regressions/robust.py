import pandas as pd


from sklearn.linear_model import (
    RANSACRegressor, HuberRegressor, 
)

from sklearn.svm import SVR

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


if __name__ == '__main__':
    
    dataset = pd.read_csv('./Data/felicidad_corrupt.csv')
    print (dataset.head(5))

    X = dataset.drop(['country', 'score'], axis=1)
    y = dataset['score']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    estimadores = {
        'SVR' : SVR(gamma='auto', C=1.0, epsilon=0.1),
        'RANSAC' : RANSACRegressor(),
        'HUBER' : HuberRegressor(epsilon=1.35)
    }

    for name, estimador in estimadores.items():
        estimador.fit(X_train, y_train)
        y_pred = estimador.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print('='*64)
        print(f'{name}: Mean Squared Error = {mse}')