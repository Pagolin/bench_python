from collections import namedtuple
from typing import List
import numpy as np
from scipy.spatial.distance import euclidean

Value = namedtuple("Value", ["values", "assoc_cluster"])
randomState = np.random.RandomState()

def read_values(file):
    with open(file) as input:
        pass


def reassign_values(v, centroids):
    pass


def evaluate_resuls(new_vals):
    pass


def should_continue(delta, threshold, iterations, max_iter):
    return delta > threshold and iterations < max_iter


def create_centroids(vals, centroids):
    """
    Create new centroids, based on the assignments of the values
    in the previous round of fitting.
    :param vals:
    :param centroids:
    :return:
    """
    pass


def init_centroids(vals, num_centroids):
    """
    Select randomly values from the
    :param vals:
    :param centroids:
    :return:
    """
    seeds = randomState.permutation(len(vals))






def inc(iterations):
    return iterations+1


def find_nearest_centroid(val: Value, centroids: List[List[float]]):
    distances = [euclidean(val.values, c_vector) for c_vector in centroids]
    best_fit = distances.index(min(distances))
    return best_fit
