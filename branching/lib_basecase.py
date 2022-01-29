from helpers.heavy_functions import allocate_and_sum_list

ORIGINAL_INPUT = 10000


def check(x):
    return x % 2 == 0


def if_fun(x):
    # print("called if with ", x)
    return allocate_and_sum_list(ORIGINAL_INPUT)


def else_fun(x):
    # print("called else with ", x)
    return allocate_and_sum_list(ORIGINAL_INPUT)

# It has to be x+1, because 0's mess up my modulo induced relations
prepare_input = lambda x: range(1, x+1)
