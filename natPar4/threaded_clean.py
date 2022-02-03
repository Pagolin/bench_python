import threading as th
from helpers.library_proxy import *


def wrapper(fun, arg, key):
    r = fun(arg)
    global results
    results[key] = r

def algo(i):
    global results
    results = {}
    fst = th.Thread(target=wrapper, args=(fun1,i,"a"))
    fst.start()
    scnd = th.Thread(target=wrapper, args=(fun2,i,"b"))
    scnd.start()
    thrd = th.Thread(target=wrapper, args=(fun3,i,"c"))
    thrd.start()
    frth = th.Thread(target=wrapper, args=(fun4, i, "d"))
    frth.start()
    result = combine(i, *results)
    fst.join()
    scnd.join()
    thrd.join()
    frth.join()
    return result

