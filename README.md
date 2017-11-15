# K-Means-Implementation

K-means on the standard iris dataset. 

The program contains 4 methods. The program is run by calling kmeans(X,N) where X is the data set and N is the number of clusters. 

The program initializes the centroids by taking random samples of the dataset.The program runs until the method converged(mu, oldmu, num_iter)is true. Once the centroids are intialized, the classify_points(X, mu) method assigns all the values in X to clusters. Then the centroid is recalculated using the calc_centroid(oldmu, clusters) method until the centroids converge.

The programs outputs:

1. The total number of iterations necessary for convergence:
2. The total number of data instances:
3. The final means of each cluster:
4. The size of each cluster:
5. The final clusters:
