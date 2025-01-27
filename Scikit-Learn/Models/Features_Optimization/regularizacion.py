# Import necessary libraries
import pandas as pd # Pandas for data manipulation and analysis
import sklearn # Machine learning library

# Import specific models and tools from sklearn
from sklearn.linear_model import LinearRegression # Linear regression model
from sklearn.linear_model import Lasso # Lasso regression model for regularization
from sklearn.linear_model import Ridge # Ridge regression model for regularization

from sklearn.model_selection import train_test_split # To split the data into training and testing sets
from sklearn.metrics import mean_squared_error # To evaluate the performance of the models

# Main execution block
if __name__ == '__main__':

    # Load the dataset from a CSV file
    dataset = pd.read_csv('./Data/felicidad.csv')

    # Display a statistical summary of the dataset
    print(dataset.describe())

    # Define feature variables (x) and target variable (y)
    X =  dataset[['gdp', 'family', 'lifexp', 'freedom', 'corruption', 'generosity', 'dystopia']] # Features for the model
    y = dataset[['score']] # Targer variable (happiness scores)

    # Print the shapes of X and y to understand their dimensions
    print(X.shape)
    print(y.shape)

    # Split the dataset into training and testing sets with a test size of 25%
    # X_train, y_train will be used to train the model
    # X_test, y_test will be used to evaluate the trained model's performance
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25)

    # Train a Linear Regression model on the training data
    modelLinear = LinearRegression().fit(X_train, y_train)
    # Make predictions on the test data using the trained Linear Regression model
    y_predict_linear =  modelLinear.predict(X_test)

    # Train a Lasso Regression model on the training data with regularization parameter alpha=0.02
    modelLasso = Lasso(alpha=0.02).fit(X_train, y_train)
    # Make predictions on the test data using the trained Lasso Regression model
    y_predict_lasso = modelLasso.predict(X_test)

    # TRain a Ridge Regression model on the training data with regularization parameter alpha=0.02
    modelRidge = Ridge(alpha=0.02).fit(X_train, y_train)
    # Make predictions on the test data using the trained Ridge Regression model
    y_predict_ridge = modelRidge.predict(X_test)

    # Calculate and print the mean squared error for the Linear Regression model
    linear_loss = mean_squared_error(y_test, y_predict_linear)
    print(f' Linear loss: {linear_loss}')

    # Calculate and print the mean squared error for the Lasso Regression model
    Lasso_loss = mean_squared_error(y_test, y_predict_lasso)
    print(f' Lasso loss: {Lasso_loss}')

    # Calculate and print the mean squared error for the Ridge Regression model
    ridge_loss = mean_squared_error(y_test, y_predict_ridge)
    print(f' Ridge Loss: {ridge_loss}')


    print('='*32)
    print('Coef LASSO')
    print(modelLasso.coef_)

    print('Coef Ridge')
    print(modelRidge.coef_)
    