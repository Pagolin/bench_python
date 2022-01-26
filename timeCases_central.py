import argparse
import time

import pandas as pd

import helpers.timing_utils as timing_utils
import natPar4
import natPar8
import natPar12
import natPar16
import natPar20
import natPar24
import natPar28
import natPar32


case_selector = {"natPar4": natPar4,
                 "natPar8": natPar8,
                 "natPar12": natPar12,
                 "natPar16": natPar16,
                 "natPar20": natPar20,
                 "natPar24": natPar24,
                 "natPar28": natPar28,
                 "natPar32": natPar32}

def timing():

def main(args):
    inputs = args.inputs
    reps = args.repetitions
    lib = args.library
    test_cases = (args.Case, case_selector[args.Case]) if args.Case \
        else case_selector.items()
    all_measurements = []
    for case_name, case in test_cases:
        measurements = case.take_times(inputs, reps, lib)
        # all_measurements.extend(measurements)
        data = pd.DataFrame(
            columns=["scenario", "version", "library", "input",
                     "reps", "time"],
            data= measurements)
        # Seconds to milliseconds
        data[["time"]] *= 1000
        file_name = args.output + "time_measures_{}_{}.csv".format(case_name,
            time.strftime("%Y_%m_%d_%I_%M"))
        data.to_csv(file_name)


def _get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--inputs",
        nargs='+',
        required=True,
        type=int,
        help="integer inputs to the algorithm. Many inputs -> Many tests "
    )
    parser.add_argument(
        "-r", "--repetitions",
        type=int,
        default=10,
        help="how often to repeat the timing",
    )
    parser.add_argument(
        "-l", "--library",
        type=str,
        default=None,
        help="which library to take the functions from. Options: {}"
            .format(timing_utils.default_libraries),
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="./",
        help=" path to write the timing measurements to ",
    )
    parser.add_argument(
        "-c", "--Case",
        type=str,
        default=None,
        help="which testcase (i.e. python package containing at least "
             "'sequential.py' and "
             "one alternative implementation) should be run"
    )
    return parser


if __name__ == '__main__':
    main(_get_argument_parser().parse_args())
