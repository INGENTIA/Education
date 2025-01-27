# Importing pandas for data manipulation and analysis
import pandas as pd

# Importing MiniBatchKMeans for clustering
from sklearn.cluster import MiniBatchKMeans

# Main execution block
if __name__ == '__main__':

    # Loading the dataset from a CSV file into a pandas DataFrame
    dataset = pd.read_csv('../Data/candy.csv')

    # Displaying the first 10 rows of the dataset for a quick preview
    print(dataset.head(10))

    # Dropping the 'competitorname' column as it's not a feature for clustering
    X = dataset.drop('competitorname', axis=1)

    # Creating and fitting a MiniBatchKMeans model with 4 clusters and a batch size of 8
    kmeans = MiniBatchKMeans(n_clusters=4, batch_size=8).fit(X)

    # Printing the total number of cluster centers
    print('Total de centros: ', len(kmeans.cluster_centers_))
    
    # Separator for a better readability
    print("="*64)

    # Predicting the cluster labels for each data point in the dataset
    print(kmeans.predict(X))

    # Adding the dataset with the newly added cluster group column
    dataset['group'] = kmeans.predict(X)

    # Displaying the dataset with the newly added cluster group column
    print(dataset)
