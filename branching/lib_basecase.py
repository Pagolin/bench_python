from helpers.heavy_functions import allocate_and_sum_list

ORIGINAL_INPUT = 10000


def check(x):
    return x % 2 == 0


def if_fun(x):
    return allocate_and_sum_list(ORIGINAL_INPUT)


def else_fun(x):
    return allocate_and_sum_list(ORIGINAL_INPUT)


def prepare_input(x):
    # It has to be x+1,
    # because 0's mess up modulo induced relations
    return range(1, x + 1)
