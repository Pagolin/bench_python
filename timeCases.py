import argparse
import time
import pandas as pd
import helpers.timing_utils as timing_utils
import natPar3.timing
import natPar7.timing
import natPar15.timing
import natPar31.timing
case_selector = {"natPar3": natPar3.timing,
                "natPar7": natPar7.timing,
                "natPar15": natPar15.timing,
                "natPar31": natPar31.timing}



def main(args):
    inputs = args.inputs
    reps = args.repetitions
    lib = args.library
    test_cases = [case_selector[args.Case]] if args.Case \
        else list(case_selector.values())
    all_measurements = []
    for case in test_cases:
        measurements = case.take_times(inputs, reps, lib)
        all_measurements.extend(measurements)
    data = pd.DataFrame(
        columns=["scenario", "version", "library", "input",
                 "reps", "min", "geo-mean", "max"],
        data=all_measurements)
    # Seconds to milliseconds
    data[["min", "geo-mean", "max"]] *= 1000
    data.to_csv(args.output)


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
        default="./time_measures_{}.csv".format(
            time.strftime("%Y_%m_%d_%I_%M")),
        help="file path to write the timing measurements to  ",
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
