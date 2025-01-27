# import necessary libraries 
import pandas as pd # Pandas for data manipulation and analysis
import sklearn # General machine learning library
import matplotlib.pyplot as plt # matplotlib for data visualization

# Import specific modules form sklear for dimensionality reduction
from sklearn.decomposition import PCA # Principal component analysis for dimensionaliry reduction
from sklearn.decomposition import IncrementalPCA # Incremental PCA for large datasets

# Import modules for machine learning and preprocessing
from sklearn.linear_model import LogisticRegression # Logistci regression for machine learning model
from sklearn.preprocessing import StandardScaler # Standarize features by removing the mean and scalin to unit variance
from sklearn.model_selection import train_test_split # Split the dataset into training and testing sets

if __name__ == '__main__':
    # Load dataset
    df_heart = pd.read_csv('./Data/heart.csv')

    # Display the first 5 rows of the dataset
    print(df_heart.head(5))

    # Separate the dataset into features and targer variable
    dt_features = df_heart.drop(['target'], axis=1) # Features )all columns except 'target')
    dt_target = df_heart['target'] # Target variable ('target' column)

    # Standardize the feature data
    dt_features =  StandardScaler().fit_transform(dt_features)
    
    # Split the data into training and testing sets
    X_train,  X_test, y_train, y_test =train_test_split(dt_features, dt_target, test_size = 0.3, random_state = 42 ) # 30% for testing, 70% for training, with a fixed random seed

    print(X_train.shape) 
    print(y_train.shape)

    # n_components = min(n_muestras, n_features)
    pca = PCA(n_components = 3)
    pca.fit(X_train)

    ipca = IncrementalPCA(n_components = 3, batch_size = 10)
    ipca.fit(X_train)

    plt.plot(range(len(pca.explained_variance_)),pca.explained_variance_ratio_)
    plt.show()

    logistic = LogisticRegression(solver= 'lbfgs')

    dt_train = pca.transform(X_train)
    dt_test = pca.transform(X_test)
    logistic.fit(dt_train, y_train)
    print(f'SCORE PCA: {logistic.score(dt_test, y_test)} ')
    
    dt_train = ipca.transform(X_train)
    dt_test = ipca.transform(X_test)
    logistic.fit(dt_train, y_train)
    print(f'SCORE IPCA: {logistic.score(dt_test, y_test)}')