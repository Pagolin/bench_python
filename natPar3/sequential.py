# from libs import lib_fannkuch
# library_proxy.set_lib(lib_fannkuch)
# fun1, fun2, fun3, combine, *others =  library_proxy.get_funs()
from helpers.library_proxy import *

def algo(i):
    x = fun1(i)
    y = fun2(i)
    z = fun3(i)
    result = combine(i, x, y, z)
    return result

# algo(10)


