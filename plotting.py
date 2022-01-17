import argparse
import os
import time

import matplotlib.axes._subplots
import numpy
import pandas as pd
import seaborn as sn
from matplotlib.axes._subplots import *
from df_utils import df_with_speedup

l = matplotlib.axes._subplots.Subplot

def set_errorbars(plot, plot_data, is_grid=False):
    x_coords = []
    y_coords = []
    dot_colors = []
    # collections are based on hue i.e. 'lines of data with same color'
    for point_pair in plot.collections:
        point_pair.set_sizes(point_pair.get_sizes() * 0.5)
        for x, y in point_pair.get_offsets():
            if type(x) != numpy.float64:
                # it's a filling for a missing point
                continue
            dot_colors.append(point_pair.get_edgecolor())
            x_coords.append(x)
            y_coords.append(y)
    colors = plot.collections[0].get_fc() if is_grid else dot_colors
    plot.errorbar(x_coords, y_coords, plot_data[["y_minus", "y_plus"]].T,
                  ecolor=colors, fmt=' ')


def set_plus_minus(plot_data, y_max, y_mean, y_min):
    plot_data.loc[:, "y_minus"] = plot_data[y_mean] - plot_data[y_min]
    plot_data.loc[:, "y_plus"] = plot_data[y_max] - plot_data[y_mean]


def set_title(plot, info, data):
    if info:
        groups = data.groupby(info)
        # complicated way to get to a list of values in the info column
        infos = groups.apply(list).index.tolist()
        if len(infos) == 1:
            plot.set_title("{}: {}".format(info, infos[0]))


def make_speedup_pointplot(data, columns, outdir,
                           outputfile, info, isGrid=False):
    speedup_data, legend_item = df_with_speedup(data, columns)
    plot = sn.pointplot(x="scenario", y="S_mean", hue=legend_item,
                        dodge=True, join=False, ci=None,
                        data=speedup_data, pallet="Paired")
    y_axis_min, y_axis_max = plot.get_ylim()
    plot.set_ylim((0, y_axis_max))
    set_plus_minus(data, y_max="S_max", y_mean="S_mean", y_min="S_min")
    set_errorbars(plot, speedup_data, isGrid)
    set_title(plot, info, speedup_data)
    plot.set(xlabel="# independent functions")
    figure = plot.get_figure()
    figure.savefig(outdir + outputfile)


def pointplot_with_errors(data: pd.DataFrame, x: str, y: str,
                          hue: str, yerr_max=None, yerr_min=None, isGrid=False,
                          **kwargs):
    plot = sn.pointplot(x=x, y=y, hue=hue,
                        dodge=True, join=False, ci=None,
                        data=data, **kwargs)
    set_errorbars(plot, data, isGrid)
    return plot

def scatterplot_with_errors(data: pd.DataFrame, x: str, y: str,
                            hue: str, yerr_max=None, yerr_min=None,
                            isGrid=False, **kwargs):

    plot = sn.scatterplot(x=x, y=y, hue=hue, ci=None,
                        data=data)
    set_errorbars(plot, data, isGrid)
    return plot

def plot_with_errors(data: pd.DataFrame, x: str, y: str, plot_kind,
                     hue: str, yerr_max=None, yerr_min=None,
                     isGrid=False, **kwargs):

    plot = plot_kind(x=x, y=y, hue=hue, data=data, **kwargs)
    set_errorbars(plot, data, isGrid)
    return plot


def multi_plots(xdata: str, ydata: str, inputdata: pd.DataFrame,
                hue_col: str, column_col: str,  plot_method=sn.scatterplot,
                yplus=None, yminus=None,
                outdir=None, **kwargs):
    grid = sn.FacetGrid(inputdata, col=column_col)
    """
    grid.map_dataframe(scatterplot_with_errors, x=xdata, y=ydata, hue=hue_col,
                      yerr_min=yminus, yerr_max=yplus, isGrid=True, jitter="0.2")
    """
    grid.map_dataframe(plot_with_errors, x=xdata, y=ydata, hue=hue_col,
                       plot_kind=plot_method,
                       yerr_min=yminus, yerr_max=yplus, isGrid=True, **kwargs)

    #print("axes dict: ", grid.axes_dict)
    #print("row_names: ", grid.row_names)
    #print("col_names: ", grid.col_names)

    #for ax in grid.axes_dict.values():
     #   ax.set_xticks([3,7,15,31])
      #  print(type(ax))

    grid.add_legend(title=hue_col)

    if outdir:
        grid.figure.savefig(outdir)
    else:
        grid.figure.show()


def main(args):
    inputfile = args.Input
    outdir = args.outputdir
    outputfile = args.filename
    info = args.info
    columns = args.indexcolumns
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    data = pd.read_csv(inputfile, index_col=0)
    make_speedup_pointplot(data, columns, outdir, outputfile, info)

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
        help="name of base case for speedup calculation, e.g. 'sequential' ",
    )
    parser.add_argument(
        "-i", "--info",
        type=str,
        default="input",
        help="column name to include as an info below the plot"
    )
    parser.add_argument(
        "-c", "--indexcolumns",
        nargs='+',
        required=True,
        default=["version", "library"],
        help="column(s) to use a data rows. Multiple columns will be combined"
             "as col1Value_col2Value"
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

