from kmeans_lib import *


def cluster(values, centroids, threshold, iterations, max_iterations):
    new_values = []
    # with list comprehension
    # new_values = [reassign_values(v, centroids) for v in values]
    for v in values:
        n = reassign_values(v, centroids)
    (vals, delta) = evaluate_resuls(new_values)
    condition = should_continue(delta, threshold, iterations, max_iterations)
    (new_vals, new_centroids) = create_centroids(vals, centroids)
    inc_iter = inc(iterations)
    if condition:
        return cluster(new_vals, new_centroids, threshold, inc_iter)
    else:
        return inc_iter

def calculate(values, centroids, threshold, iterations, max_iterations):
    return calculate(values, centroids, threshold, iterations, max_iterations)