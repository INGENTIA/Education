# Importing pandas for data manipulation and analysis
import pandas as pd

# Importing RandomizedSearchCV for hyperparameter tuning
from sklearn.model_selection import RandomizedSearchCV

# Importing RandomForestRegressor for regression tasks
from sklearn.ensemble import RandomForestRegressor

# Main execution block
if __name__ == '__main__':

    # Loading the dataset from a CSV file into a pandas DataFrame
    dataset = pd.read_csv('../Data/felicidad.csv')

    # Displaying the first 10 rows of the dataset for a quick preview
    print(dataset.head(10))

    # Separating features (X) and target variable (y)
    # Dropping the 'country', 'ranl', and 'score' colums from features
    X = dataset.drop(['country', 'rank', 'score'], axis=1)

    # Setting the target variable as the 'score' column
    y = dataset['score']

    # Creating a Random Forest Regressor model
    reg = RandomForestRegressor()

    # Defining a parameter grid for hyperparameter tunin
    parametros = {
        'n_estimators' : range(4,16), # Number of trees in the forest (4 to 15 inclusive)
        'criterion' :['squared_error', 'absolute_error'], # Splitting criteria: mean squared error or mean absolute error
        'max_depth' : range(2,11) # Maximum depth of each tree (2 to 10 inclusive)
    }

    # Creating and fitting a RandomizedSearchCV object for hyperparameter tunning
    rand_est = RandomizedSearchCV(reg, parametros, n_iter=10, cv=3, scoring='neg_mean_absolute_error').fit(X,y)

    # Printing the best estimator found during the random search
    print(rand_est.best_estimator_)

    print(rand_est.best_params_)

    print(rand_est.predict(X.loc[[0]]))
                                