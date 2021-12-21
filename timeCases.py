import pandas as pd
import helpers.timing_utils as timing_utils
import natPar3.timing
import natPar7.timing
import natPar15.timing
import natPar32.timing
from natPar7 import timing as timing7
case_selector = {"natPar3": natPar3.timing,
                "natPar7": natPar7.timing,
                "natPar15": natPar15.timing,
                "natPar32": natPar32.timing}


def main(args):
    pSize = args.Input
    reps = args.repetitions
    lib = args.library
    test_cases = [case_selector[args.Case]] if args.Case \
        else list(case_selector.values())
    all_measurements = []
    for case in test_cases:
        measurements = case.take_times(pSize, reps, lib)
        all_measurements.extend(measurements)
    data = pd.DataFrame(
        columns=["scenario", "version", "library", "input",
                 "reps", "min", "geo-mean", "max"],
        data=all_measurements)
    data.to_csv(args.output)


def _get_argument_parser():
    parser = timing_utils.get_argument_parser()
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
