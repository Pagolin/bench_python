import timeit, time
import importlib
import argparse
import pandas as pd
from statistics import median, geometric_mean

from helpers import library_proxy
from helpers.timing_utils import default_libraries, Version, lib_select

import natPar15.sequential as sequential
import natPar15.compiled as compiled
import natPar15.algo as algo


versions = [Version("sequential", sequential, []),
            Version("compiled", compiled, [algo])]


def take_times(inputs, reps, lib_arg= None, pname=__name__):
    global input

    libraries = [lib_arg] if lib_arg \
        else [name for name in lib_select.keys()]

    all_measurements = []

    for version in versions:
        for library in libraries:
            # determine which library functions are exported by library_proxy,
            # when the algorithms import library proxy
            library_proxy.set_lib(lib_select[library])
            # reload the module to link the new library
            importlib.reload(version.module)
            [importlib.reload(mod) for mod in version.dependent_modules]
            for input in inputs:
                test_params = [pname, version.name,
                               library, input, reps]
                setup = "from {} import input, library_proxy, {};" \
                    .format(__name__, version.name)
                times = timeit.Timer(
                    stmt="{}.algo(input)".format(version.name),
                    setup=setup) \
                    .repeat(reps, number=1)
                print("{} with {} done in {}".format(version.name, library,
                                                     median(times)))
                measurements = [min(times), geometric_mean(times), max(times)]
                all_measurements.append(test_params + measurements)
    return all_measurements


def main(args):
    inputs = args.inputs
    reps = args.repetitions
    lib = args.library
    measurements = take_times(inputs, reps, lib, "natPar15")
    # prepare data collection
    data = pd.DataFrame(
        columns=["scenario", "version", "library", "input",
                 "reps", "min", "geo-mean", "max"],
        data=measurements)
    # Seconds to milliseconds
    data[["min", "geo-mean", "max"]] *= 1000
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

if __name__ == '__main__':
    main(get_argument_parser().parse_args())

