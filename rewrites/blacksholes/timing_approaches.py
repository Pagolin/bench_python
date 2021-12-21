import argparse
import pandas as pd
from timeit import Timer
from bs_lib import Option
from bs_main import calculate
from bs_main_compiled import calulate as calculate_par

# TODO: By default Timer uses time.perf_counter() which really counts the
#  time between to points, time.process_time() measures the of the
#  sum of the system and user CPU time of the current process.
#  It does not include time elapsed during sleep.
#  It is process-wide by definition.  -> consider switching, what does
#  'process-wide' mean in multi-processing setting


def loadDataFrame(file):
    data = pd.read_csv(file, sep=" ",
                       names=["spot", "strike", "risk_free_rate",
                              "dividende_rate", "volatility", "time", "ty",
                              "dividende_false", "ref_val"])
    return data


def asOptionsList(file):
    data_frame = loadDataFrame(file)
    as_array = [Option(*row) for (index, row) in data_frame.iterrows()]
    return as_array


def main(args):
    file = args.FILE
    reps = args.repetitions
    global optionsList
    optionsList = asOptionsList(file)
    setup = """from __main__ import calculate, calculate_par, optionsList"""
    seqTimes = Timer(stmt="calculate(optionsList)", setup=setup)\
        .repeat(reps, number=1)
    print(min(seqTimes))
    parTimes = Timer(stmt="calculate_par(optionsList)", setup=setup)\
        .repeat(reps, number=1)
    print(min(parTimes))

def _get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "FILE",
        type=argparse.FileType("r"),
        help="file with option data",
    )
    parser.add_argument(
        "-r", "--repetitions",
        type=int,
        default=30,
        help="how often to repeat the timing",
    )
    return parser


if __name__ == '__main__':
    main(_get_argument_parser().parse_args())
