import argparse
import importlib
import time
import timeit
from math import ceil, floor
from statistics import median

import pandas as pd

import branching.algo as algo
import branching.branch_lib_proxy as lp
import branching.compiled as compiled
import branching.sequential as sequential
import branching.lib_basecase as basecase
from branching.tooling import make_even_blocks, distribute_even
from helpers.heavy_functions import allocate_and_sum_list
from helpers.timing_utils import Version

lp.set_lib(basecase)

versions = [Version("sequential", sequential, []),
            Version("compiled", compiled, [algo])]

# Relations should be  1:1, 1:2, 1:4, 1:8 and 1:0
# We expect speedup to decrease as relations get more uneven
relations = [2, 3, 5, 9, 1]
interesting_blocksizes = {2: 1, 3: 50, 5: 100, 9: 150, 1: 200}


def set_check(rel):
    lp.check = lambda x: x % rel == 0


def set_if_else(rel):
    complexity_for_both = 2*basecase.ORIGINAL_INPUT
    lp.if_fun = lambda x: allocate_and_sum_list(
        ceil(1 / rel * complexity_for_both))
    lp.else_fun = lambda x: allocate_and_sum_list(
        floor((rel - 1) / rel * complexity_for_both))


def set_prepare_input(rel, function):
    lp.prepare_input = lambda input: function(input, rel)


def take_times(inputs, reps, lib_arg=None, pname=__name__):
    global command_input, input
    all_measurements = []
    for version in versions:
        for rel in relations:
            # Measure different Branching relations

            set_check(rel)
            measurements = measure_current_lib(
                inputs, pname, "check relation", rel, reps, version)
            all_measurements.extend(measurements)
            lp.set_lib(basecase)
            
           # Measure different relations of branch runtimes
            set_if_else(rel)
            measurements = measure_current_lib(
                inputs, pname, "branch time relation", rel, reps, version)
            all_measurements.extend(measurements)
            lp.set_lib(basecase)

            # Measure different distributions of if-else cases in the input
            set_prepare_input(rel, distribute_even)
            measurements = measure_current_lib(
                inputs, pname, "case distribution", rel, reps, version)
            all_measurements.extend(measurements)
            lp.set_lib(basecase)

            # Measure different blocksizes of if-else cases in the input
            # i.e. 1: if->else->if->else.. vs 2: if-> if-> else->else-> ...
            block_size = interesting_blocksizes[rel]
            set_prepare_input(block_size, make_even_blocks)
            measurements = measure_current_lib(
                inputs, pname, "case block size ", block_size, reps, version)
            all_measurements.extend(measurements)
            lp.set_lib(basecase)

    return all_measurements


def measure_current_lib(inputs, pname, altered, rel, reps, version):
    global command_input, input
    current_measurements = []
    # reload the module to link the new library
    importlib.reload(version.module)
    [importlib.reload(mod) for mod in version.dependent_modules]
    for command_input in inputs:
        test_params = \
            [pname, version.name, altered, rel, command_input, reps]
        input = lp.prepare_input(command_input)
        setup = "from {} import input, lp, {};" \
            .format(__name__, version.name)
        times = timeit.Timer(
            stmt="{}.algo(input)".format(version.name),
            setup=setup) \
            .repeat(reps, number=1)
        print("{} with modified {} = {}: done in {}".format(version.name,
                                             altered, str(rel),
                                             median(times)))
        for time in times:
            current_measurements.append(test_params + [time])
    return current_measurements


def main(args):
    inputs = args.inputs
    reps = args.repetitions
    measurements = take_times(inputs, reps, pname="branching")
    # prepare data collection
    data = pd.DataFrame(
        columns=["scenario", "version", "modified function", "value", "input",
                 "reps", "time"],
        data=measurements)
    data["list function input"] = basecase.ORIGINAL_INPUT
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
