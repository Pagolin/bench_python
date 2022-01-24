from concurrent.futures import ThreadPoolExecutor
from helpers import library_proxy
from helpers.timing_utils import get_argument_parser, lib_select

def wrapper(fun, arg, pos):
    r = fun(arg)
    global result_list
    result_list[pos] = r

def algo(i):
    global result_list
    with ThreadPoolExecutor() as e:
        fst = e.submit(fun1,i)
        scnd = e.submit(fun2,i)
        thrd = e.submit(fun3,i)
        frth = e.submit(fun4, i)
    a = fst.result()
    b = scnd.result()
    c = thrd.result()
    d = frth.result()
    result = combine(i, a, b, c, d)
    return result


if __name__ == '__main__':
    args = get_argument_parser().parse_args()
    input = args.Input
    library_proxy.set_lib(lib_select[args.library])
    global fun1, fun2, fun3,fun4, combine
    fun1, fun2, fun3,fun4, combine, *other = library_proxy.get_funs()
    result = algo(input)
    print(result)

