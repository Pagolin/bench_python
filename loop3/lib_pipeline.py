import random

from helpers.heavy_functions import isprime


def fun1(i):
    l = [random.randint(0, 1000) for _ in range(1000000)]
    return l


def fun2(x):
    # sort it
    x.sort()
    return x

def fun3(x):
    # filter for primes
    iterator = filter(isprime, x)
    s = sum(iterator)
    return s
