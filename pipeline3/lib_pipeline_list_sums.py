from helpers.heavy_functions import allocate_and_sum_list

# Those functions should be pipelined but
# retain the same complexity as their task parallel
# equivalent, i.e we want to show scaling based on the
# number of loops the pipeline is executed in.
# So for now we just ignore the input,
# which is used to scale the number of loops here
def prepare_input(x):
    return x

def fun1(x):
    if x != 100:
        x = 100
    return allocate_and_sum_list(x*1000)


def fun2(x):
    if x != 100:
        x = 100
    return allocate_and_sum_list(x*1000)


def fun3(x):
    if x != 100:
        x = 100
    return allocate_and_sum_list(x*1000)

fun_default = fun1
def combine(*args):
    pass


def check(x):
    pass


def elseFun(x):
    pass

