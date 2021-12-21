import os
import numpy
import argparse
import time
import pandas as pd
import seaborn as sn

pd.set_option('display.max_columns', 16)


def prepare_dataframe(data):
    basevalues = data[data.version == "sequential"]

    # join dataframes such that every measurement
    # has the according sequential measurement in the same row
    compared_to_sequential = data.merge(
        basevalues[["scenario", "library", "min", "geo-mean", "max"]],
        on=["scenario", "library"],
        suffixes=('', '_seq'))

    # minimal speedup = maximal parallel time / minimal sequential time
    compared_to_sequential["S_min"] = compared_to_sequential["min_seq"] \
                                      / compared_to_sequential["max"]
    # maximal speedup = minimal parallel time / maximal sequential time
    compared_to_sequential["S_max"] = compared_to_sequential["max_seq"] \
                                      / compared_to_sequential["min"]
    # mean speedup = mean parallel time / mean sequential time
    compared_to_sequential["S_mean"] = compared_to_sequential["geo-mean_seq"] \
                                       / compared_to_sequential["geo-mean"]

    # Remove sequential results from speedup plot
    compared_to_sequential = compared_to_sequential[compared_to_sequential["version"] != "sequential"]
    # Make one column 'version - library' for hue
    compared_to_sequential["version_lib"] = compared_to_sequential["version"] + "_" + compared_to_sequential["library"]

    print("Prepared Data:")
    pO = compared_to_sequential[["scenario","version_lib", "S_min", "S_mean", "S_max", "min", "geo-mean", "max",  "min_seq", "geo-mean_seq", "max_seq"]].sort_values("version_lib")
    print(pO)
    return compared_to_sequential


def set_errorbars(plot, plot_data):
    x_coords =[]
    y_coords =[]
    colors = []
    # collections are based on hue i.e. version_lib combinations
    for point_pair in plot.collections:
        point_pair.set_sizes(point_pair.get_sizes()*0.5)
        for x, y in point_pair.get_offsets():
            if type(x) != numpy.float64:
                # it's a filling for a missing point
                continue
            colors.append(point_pair.get_edgecolor())
            x_coords.append(x)
            y_coords.append(y)
    plot_data["y_minus"] = plot_data["S_mean"] - plot_data["S_min"]
    plot_data["y_plus"]  = plot_data["S_max"] - plot_data["S_mean"]

    plot.errorbar(x_coords, y_coords, plot_data[["y_minus", "y_plus"]].T,
                  ecolor=colors, fmt=' ')


def main(args):
    inputfile = args.Input
    outdir = args.outputdir
    outputfile = args.filename
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    data = pd.read_csv(inputfile, index_col=0)
    speedup_data = prepare_dataframe(data)
    plot = sn.pointplot(x="scenario", y="S_mean", hue="version_lib",
                        style="library",
                        dodge=True, join=False, ci=None,
                        data=speedup_data)
    set_errorbars(plot, speedup_data)
    figure = plot.get_figure()
    figure.savefig(outdir + outputfile)





def _get_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "Input",
        type=str,
        help="path of data file in csv format",
    )
    parser.add_argument(
        "-b", "--base-case",
        type=str,
        help="name of base case for speedup calculation, ",
    )
    parser.add_argument(
        "-o", "--outputdir",
        type=str,
        default="./",
        help="output file path",
    )
    parser.add_argument(
        "-f", "--filename",
        type=str,
        default="bm_plot_{}".format(time.strftime("%Y_%m_%d_%I_%M")),
        help="name of output file"
    )
    return parser



if __name__ == '__main__':
    main(_get_argument_parser().parse_args())
    

