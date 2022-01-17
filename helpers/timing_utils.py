import argparse
import time, timeit
import importlib
from collections import namedtuple
from libs import lib_sleep, lib_pass, lib_fannkuch, \
    lib_lists, lib_list_sum, lib_list_IO

default_libraries = {"sleep", "fannkuch", "lists", "list_sum", "list_io"}
Version = namedtuple('Version', 'name, module, dependent_modules')
"""
lib_select = {"sleep": lib_sleep, "fannkuch": lib_fannkuch, "lists": lib_lists,
              "list_sum": lib_list_sum, "list_io": lib_list_IO,
              "pass": lib_pass}
              
"""
lib_select = {"lists": lib_lists,
              "list_sum": lib_list_sum, "list_io": lib_list_IO, "pass": lib_pass}

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
        help="which library to take the functions from. Options: {}"
            .format(default_libraries),
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="./time_measures_{}.csv".format(
            time.strftime("%Y_%m_%d_%I_%M")),
        help="file path to write the timing measurements to  ",
    )
    return parser
