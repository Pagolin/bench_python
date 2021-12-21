import threading as th
from helpers import library_proxy
from helpers.timing_utils import get_argument_parser, lib_select

def wrapper(fun, arg, pos):
    r = fun(arg)
    global result_list
    result_list[pos] = r

def algo(i):
    global result_list
    result_list = [None, None, None]
    fst = th.Thread(target=wrapper, args=(fun1,i,0))
    fst.start()
    scnd = th.Thread(target=wrapper, args=(fun2,i,1))
    scnd.start()
    thrd = th.Thread(target=wrapper, args=(fun3,i,2))
    thrd.start()
    result = combine(i, *result_list)
    fst.join()
    scnd.join()
    thrd.join()
    return result


if __name__ == '__main__':
    args = get_argument_parser().parse_args()
    input = args.Input
    library_proxy.set_lib(lib_select[args.library])
    global fun1, fun2, fun3, combine
    fun1, fun2, fun3, combine, *other = library_proxy.get_funs()
    result = algo(input)
    print(result)

