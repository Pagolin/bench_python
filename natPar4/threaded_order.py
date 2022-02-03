import threading as th
from helpers import library_proxy
from helpers.library_proxy import *
from helpers.timing_utils import lib_select
import time
import argparse


def wrapper(fun, arg, key):
    r = fun(arg)
    global results
    results[key] = r

def algo(i):
    global results
    results = {}
    fst = th.Thread(target=wrapper, args=(fun1,i,"a"))
    scnd = th.Thread(target=wrapper, args=(fun2,i,"b"))
    thrd = th.Thread(target=wrapper, args=(fun3,i,"c"))
    frth = th.Thread(target=wrapper, args=(fun4, i, "d"))
    fst.start()
    scnd.start()
    thrd.start()
    frth.start()
    result = combine(i, *results)
    fst.join()
    scnd.join()
    thrd.join()
    frth.join()
    return result



def get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--inputs",
        nargs='+',
        type=int,
        required=True,
        action='append',
        help="integer inputs to the algorithm. Many inputs -> Many tests "
    )
    parser.add_argument(
        "-r", "--repetitions",
        type=int,
        default=20,
        help="how often to repeat the timing",
    )
    parser.add_argument(
        "-l", "--library",
        type=str,
        default=None,
        help="which library to take the functions from. Options: ",
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="./time_measures_{}.csv".format(
            time.strftime("%Y_%m_%d_%I_%M")),
        help="file path to write the timing measurements to  ",
    )
    return parser



if __name__ == '__main__':
    args = get_argument_parser().parse_args()
    inputs = args.inputs
    library_proxy.set_lib(lib_select[args.library])
    global fun1, fun2, fun3,fun4, combine
    fun1, fun2, fun3, fun4, combine, *other = library_proxy.get_funs()
    result = algo(inputs[0][0])


