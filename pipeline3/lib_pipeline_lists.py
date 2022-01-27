from helpers.heavy_functions import allocate_list

# Those functions should be pipelined but
# retain the same complexity as their task parallel
# equivalent, i.e we want to show scaling based on the
# number of loops the pipeline is executed in.
# So for now we just ignore the input,
# which is used to scale the number of loops here
def prepare_input(x):
    return x

def fun1(x):
    y = 1
    if x == 1:
        y = x
    return allocate_list(y*1000)

def fun2(x):
    y = 1
    if x[0] == 1:
        y = x[0]
    return allocate_list(y * 1000)

def fun3(x):
    y = 1
    if x[0] == 1:
        y = x[0]
    return allocate_list(y * 1000)

fun_default = fun1
def combine(*args):
    pass


def check(x):
    pass


def elseFun(x):
    pass

