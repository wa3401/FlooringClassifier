import pandas as pd
from sklearn.cluster import KMeans

def k_means(data_path): 
    # Read the csv file containing image data
    df = pd.read_csv(data_path)

    # Extract the mean and median values for clustering
    mean_data = df[['rMean', 'gMean', 'bMean']]
    median_data = df[['rMedian', 'gMedian', 'bMedian']]

    # Define the number of clusters
    num_clusters = 3

    # Initialize the k-means algorithm
    kmeans_mean = KMeans(n_clusters=num_clusters, random_state=0)
    kmeans_median = KMeans(n_clusters=num_clusters, random_state=0)

    # Fit the k-means algorithm to the data
    kmeans_mean.fit(mean_data)
    kmeans_median.fit(median_data)

    # Add the cluster labels to the dataframe
    df['cluster_mean'] = kmeans_mean.labels_
    df['cluster_median'] = kmeans_median.labels_

    # Save the updated dataframe to a new csv file
    df.to_csv('image_data_clustered.csv', index=False)

k_means('../data/image_data.csv')