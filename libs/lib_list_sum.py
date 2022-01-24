from helpers.heavy_functions import allocate_and_sum_list
import time

def prepare_input(x):
    return x*100

def fun1(x):
    return allocate_and_sum_list(x*1000)


def fun2(x):
    return allocate_and_sum_list(x*1000)


def fun3(x):
    return allocate_and_sum_list(x*1000)

fun_default = fun1

def combine(*args):
    x, *rest = args
    return x


def check(x):
    return True


def elseFun(x):
    return allocate_and_sum_list(x*1000)


def dummy():
    time.sleep(1)

