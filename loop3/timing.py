import timeit
import time
import importlib
import argparse
import pandas as pd
from statistics import median

from helpers.timing_utils import Version
import loop3.lib_pipeline as lib_pipeline
import loop3.sequential as sequential
import loop3.compiled as compiled
import loop3.algo as algo

versions = [Version("sequential", sequential, []),
            Version("compiled", compiled, [algo])]


def take_times(inputs, reps, lib_arg= None, pname=__name__):
    global input

    libraries = [lib_pipeline]
    all_measurements = []

    for version in versions:
        for library in libraries:
            # reload the module to link the new library
            importlib.reload(version.module)
            [importlib.reload(mod) for mod in version.dependent_modules]
            for input in inputs:
                test_params = [pname, version.name,
                               library, input, reps]
                setup = "from {} import input, {};" \
                    .format(__name__, version.name)
                times = timeit.Timer(stmt="{}.algo(input)".format(version.name),
                                     setup=setup) \
                    .repeat(reps, number=1)
                print("{} with {} done in {}".format(version.name, library,
                                                     median(times)))
                for time in times:
                    all_measurements.append(test_params + [time])
    return all_measurements


def main(args):
    inputs = args.inputs
    reps = args.repetitions
    measurements = take_times(inputs, reps, None, "loop3")
    # prepare data collection
    data = pd.DataFrame(
        columns=["scenario", "version", "library", "input",
                 "reps", "time"],
        data=measurements)
    # Seconds to milliseconds
    data[["time"]] *= 1000
    data.to_csv(args.output)


def get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--inputs',
        nargs='+',
        type=int,
        required=True,
        help="integer inputs to the algorithm. Many inputs -> Many tests "
    )
    parser.add_argument(
        "-r", "--repetitions",
        type=int,
        default=10,
        help="how often to repeat the timing",
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
    main(get_argument_parser().parse_args())