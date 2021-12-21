import timeit
import importlib
import pandas as pd
from statistics import median, geometric_mean

from helpers import library_proxy
from helpers.timing_utils import get_argument_parser, Version, lib_select

import natPar7.sequential as sequential
import natPar7.compiled as compiled
import natPar7.algo as algo


versions = [Version("sequential", sequential, []),
            Version("compiled", compiled, [algo])]


def take_times(problemSize, reps, lib_arg= None, pname=__name__):
    global pSize
    pSize = problemSize

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

            test_params = [pname, version.name,
                           library, pSize, reps]
            setup = "from {} import pSize, library_proxy, {};" \
                .format(__name__, version.name)
            times = timeit.Timer(stmt="{}.algo(pSize)".format(version.name),
                                 setup=setup) \
                .repeat(reps, number=1)
            print("{} with {} done in {}".format(version.name, library,
                                                 median(times)))
            measurements = [min(times), geometric_mean(times), max(times)]
            all_measurements.append(test_params + measurements)

    return all_measurements


def main(args):
    pSize = args.Input
    reps = args.repetitions
    lib = args.library
    measurements = take_times(pSize, reps, lib, "natPar7")
    # prepare data collection
    data = pd.DataFrame(
        columns=["scenario", "version", "library", "input",
                 "reps", "min", "geo-mean", "max"],
        data=measurements)
    data.to_csv(args.output)


if __name__ == '__main__':
    main(get_argument_parser().parse_args())

