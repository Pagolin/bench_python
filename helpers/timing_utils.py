import argparse
import time
from collections import namedtuple
from libs import lib_sleep, lib_pass, lib_fannkuch, lib_lists, lib_list_sum


default_libraries = {"lib", "lib_fannkuch", "lib_lists"}
Version = namedtuple('Version', 'name, module, dependent_modules')
lib_select = {"lib": lib_sleep, "lib_fannkuch": lib_fannkuch, "lib_lists": lib_lists,
              "lib_list_sum": lib_list_sum}

def get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--Input",
        type=int,
        default=1,
        help="integer representing the problem size "
             "(depending on test e.g. length of lists)",
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
        default="lib",
        help="which library to take the functions from. Options: {}"
            .format(default_libraries),
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="./time_measures_{}".format(time.strftime("%Y_%m_%d_%I_%M")),
        help="file path to write the timing measures to  ",
    )
    return parser

