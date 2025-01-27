# Importing pandas for data manipulation and analysis
import pandas as pd 

# Importing Gradient Boosting Classifier for supervised learning
from sklearn.ensemble import GradientBoostingClassifier

# Importing utility functions for model training and evaluation
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Main execution block
if __name__ == '__main__':

    # Loading the dataset from a CSV file
    dt_heart = pd.read_csv('./Data/heart.csv')

    # Displaying basic statistics for the 'target' column (the targer variable)
    print(dt_heart['target'].describe())

    # Separating the dataset into features (X) and target (y) variable
    X = dt_heart.drop(['target'], axis=1) # All column except 'target' are features
    y = dt_heart['target'] # 'target' column is the label

    # Splitting the dataset into training and testing sets with a 65%-35% ratio
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35)

    # Training a Gradient Boosting Classifier model on the training data
    boost = GradientBoostingClassifier(n_estimators=50).fit(X_train, y_train)
    
    # Making predictions on the testing set using the trained model
    boost_pred = boost.predict(X_test)

    # Displaying the accuracy of the Gradient Boosting Classifier model
    print("="*64) # Visual separator for better readability
    print(accuracy_score(boost_pred, y_test)) # Prints the accuracy of the model