import timeit
import time
import importlib
import argparse
import pandas as pd
from statistics import median

from helpers.timing_utils import Version
from helpers import library_proxy
import pipeline3.sequential as sequential
import pipeline3.compiled as compiled
import pipeline3.algo as algo

from pipeline3 import lib_pipeline_lists as lib_lists
from pipeline3 import lib_pipeline_list_sums as lib_list_sum
from pipeline3 import lib_pipeline_lists_io as lib_list_IO
from libs import lib_pass


versions = [Version("sequential", sequential, []),
            Version("compiled", compiled, [algo])]

default_libraries = {"lists", "list_sum", "list_io", "pass"}

lib_select = {"lists": lib_lists,
              "list_sum": lib_list_sum, "list_io": lib_list_IO,
              "pass": lib_pass}

def take_times(inputs, reps, lib_arg= None, pname=__name__, gc=False):
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
                setup = "from {} import input, {};" \
                    .format(__name__, version.name)
                if gc:
                    setup = setup + "gc.enable()"
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
    gc = True if args.gc else False
    measurements = take_times(inputs, reps, None, "pipeline3", gc)
    # prepare data collection
    data = pd.DataFrame(
        columns=["scenario", "version", "library", "input",
                 "reps", "time"],
        data=measurements)
    # Seconds to milliseconds
    data[["time"]] *= 1000
    file_name = args.output + "time_measures_pipeline3_{}.csv".format(
                                                               time.strftime(
                                                                   "%Y_%m_%d_%I_%M"))
    data.to_csv(file_name)


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
        "--gc",
        default=None,
        help="enable garbage collection during measurement",
        action='store_true',
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="./",
        help="path to write the timing measurements to",
    )
    return parser

if __name__ == '__main__':
    main(get_argument_parser().parse_args())