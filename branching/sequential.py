from helpers.library_proxy import *
def double(x):
    return x,x

def inner(i):
    c = fun1(i)
    flag, current  = double(c)
    return fun2(current) if check(flag) else fun3(current)

def algo(i):
    result = []
    for j in range(i):
        d = inner(j)
        result.append(d)
    return result