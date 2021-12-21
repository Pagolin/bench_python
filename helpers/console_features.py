import argparse
from libs import lib_sleep, lib_pass, lib_fannkuch

lib_select = {"lib": lib, "lib_pass": lib_pass, "lib_fannkuch": lib_fannkuch}

def get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--Input",
        type=int,
        default=1
    )
    parser.add_argument(
        "-l", "--library",
        type=str,
        default="lib",
        help="which library to take the functions from. Options: {}"
            .format(lib_select.keys()),
    )
    return parser

