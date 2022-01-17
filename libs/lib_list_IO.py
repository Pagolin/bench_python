from helpers.heavy_functions import allocate_and_write_to_file
import time

def prepare_input(x):
    return x*100

def fun1(x):
    return allocate_and_write_to_file(x*10000)


def fun2(x):
    return allocate_and_write_to_file(x*10000)


def fun3(x):
    return allocate_and_write_to_file(x*10000)

fun_default = fun1

def combine(*args):
    x, *rest = args
    return x


def ifFun(x):
    return allocate_and_write_to_file(x*10000)


def elseFun(x):
    return allocate_and_write_to_file(x*10000)


def dummy():
    time.sleep(1)

