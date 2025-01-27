# Importing pandas for data manipulation and analysis
import pandas as pd

# Importing MeanShift for clustering
from sklearn.cluster import MeanShift

# Main execution block
if __name__ == '__main__':

    # Loading the dataset from a CSV file into a pandas DataFrame
    dataset = pd.read_csv('../Data/candy.csv')

    # Displaying the first 10 rows of the dataset for a quick preview
    print(dataset.head(10))

    # Dropping the 'competitorname' column as it's not a feature for clustering
    X = dataset.drop('competitorname', axis=1)

    # Creating and fitting a MeanShift model
    meanshift = MeanShift().fit(X)

    # Printing the number of clusters identified by MeanShift
    print(max(meanshift.labels_))

    # Printing the cluster labels for each data point in the dataset
    print(meanshift.labels_)

    # Printing the cluster centers identified by MeanShift
    print(meanshift.cluster_centers_)

    # Adding a new column 'meanshift' to the dataset to store the cluster labels
    dataset['meanshift'] = meanshift.labels_

    # Separator for better readability
    print("="*64)

    # Displaying the dataset with the newly added meanshift cluster group column
    print(dataset)