# Importing pandas for data manipulation and analysis
import pandas as pd 

# Importing machine learning models: K-Nearest Neighbors and Bagging Classifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import BaggingClassifier

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

    # Training a K-Nearest Neighbors model on the training data
    knn_class = KNeighborsClassifier().fit(X_train, y_train)
    
    # Making predictions with the trained KNN model 
    knn_pred = knn_class.predict(X_test)

    # Displaying the accuracy of the KNN model
    print("="*64) # Visual Separator
    print(accuracy_score(knn_pred, y_test)) # Compares predicted labels to actual labels

    # Training a Bagging Classifier with 50 K-Nearest Neighbors estimators on the training data
    bag_class = BaggingClassifier(estimator=KNeighborsClassifier(), n_estimators = 50).fit(X_train, y_train)
    
    # Making Predictions with the trained Bagging model
    bag_pred =  bag_class.predict(X_test)

    # Displaying the accuracy of the Bagging model
    print("="*64) # Visual separator
    print(accuracy_score(bag_pred, y_test)) # Compares predicted labels to actual labels