from helpers.heavy_functions import fannkuch
import time

def prepare_input(x):
    return x

def fun1(x):
    return fannkuch(x)


def fun2(x):
    return fannkuch(x)


def fun3(x):
    return fannkuch(x)

fun_default = fun1

def combine(*args):
    x, a, b, c, *other = args
    return a == b == c


def ifFun(x):
    return fannkuch(x)


def elseFun(x):
    return fannkuch(x)


def dummy():
    time.sleep(1)

