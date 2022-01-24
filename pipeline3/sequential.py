from helpers.library_proxy import *


def algo(i):
    result = []
    for j in range(0, i):
        x = fun1(j)
        y = fun2(x)
        z = fun3(y)
        result.append(z)
    return result
