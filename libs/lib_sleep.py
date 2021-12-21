import time

def prepare_input(x):
    return x/20

def fun1(x):
    time.sleep(x / 20)


def fun2(x):
    time.sleep(x / 20)


def fun3(x):
    time.sleep(x / 20)

fun_default = fun1


def combine(*args):
    x, *other = args
    time.sleep(x / 20)


def ifFun(x):
    time.sleep(x / 20)


def elseFun(x):
    time.sleep(x / 20)
