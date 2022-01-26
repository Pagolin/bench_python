from branching.branch_lib_proxy import *

def inner(i):
    c1, c2 = double(i)
    flag = id_fun(c1)
    current = id_fun(c2)
    return if_fun(current) if check(flag) else else_fun(current)

def algo(i):
    result = []
    # we actually input an iterable, but need to wrap it for Ohua
    for j in list(i):
        d = inner(j)
        result.append(d)
    return result
