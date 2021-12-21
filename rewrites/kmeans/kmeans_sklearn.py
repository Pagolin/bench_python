from sklearn.cluster import KMeans


def kmeans(num_cl, input, threshold, max_iter):
    # TODO: Change 'random' to 'k-means++' depending on how initial
    #  centroids are created in the ohua input to maintain comparability
    return KMeans(n_clusters=num_cl, init='randomm', tol=threshold,
                  max_iter=max_iter).fit(input)
