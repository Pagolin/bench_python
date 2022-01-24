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
fun4, fun5, fun6, fun7, fun8, fun9, fun10, fun11, \
fun12, fun13, fun14, fun15 = [fun_default] * 12

def combine(*args):
    x, *other = args
    time.sleep(x / 20)


def check(x):
    return True


def elseFun(x):
    time.sleep(x / 20)
