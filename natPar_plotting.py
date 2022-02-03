from math import ceil

from plotting import *
NUM_CORES_TEST_MACHINE = 24

natPar_df = pd.read_csv(data_dir + natPars, index_col=0)


no_pass = natPar_df[natPar_df["library"] != "pass"]
only_seq_vs_comp = no_pass[
    (no_pass["version"] == "sequential")
    | (no_pass["version"] == "compiled")]

# Plot Speedup
with_speedup = add_speedup(only_seq_vs_comp, ["scenario", "library", "input"])
multi_plots(xdata="# independent functions", ydata='speedup',
            inputdata=with_speedup,
            plot_method=sns.pointplot, hue_col="input",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            **pointplot_error_args
            )


# Assume the combine function is basically negligible
# -> perfect speedup = #parallel tasks / ceil(#paralell tasks/#cores) *

def perfect_speedup(num_cores, num_funs):
    return num_funs / (ceil(num_funs/num_cores))


with_speedup["perfect speedup"] = with_speedup[
    "# independent functions"].apply(lambda n: perfect_speedup(NUM_CORES_TEST_MACHINE, n))

with_speedup["% of perfect speedup"] = with_speedup["speedup"] \
                                       / with_speedup["perfect speedup"] \
                                       * 100
multi_plots(xdata="# independent functions", ydata="% of perfect speedup",
            inputdata=with_speedup, subTitle="assumption: cores ~ core threads",
            plot_method=sns.pointplot, hue_col="input",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            palette=inputs_pallet, **pointplot_error_args
            )

# Assume only real cores do really scale
with_speedup["perfect speedup"] = with_speedup[
    "# independent functions"].apply(lambda n: perfect_speedup(12, n))

with_speedup["% of perfect speedup"] = with_speedup["speedup"] \
                                       / with_speedup["perfect speedup"] \
                                       * 100
multi_plots(xdata="# independent functions", ydata="% of perfect speedup",
            inputdata=with_speedup,
            subTitle="assumption: only real cores scale",
            plot_method=sns.pointplot, hue_col="input",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            palette=inputs_pallet, **pointplot_error_args
            )

only_seq_comp = natPar_df[
    (natPar_df["version"] == "sequential")
    | (natPar_df["version"] == "compiled")]
without_pass = only_seq_comp[only_seq_comp["library"]!= 'pass']
with_time_diff, tdiff = relative_to_list(without_pass,
                                         column="time in ms",
                                         eq_columns=["scenario", "version", "input"])

multi_plots(xdata="# independent functions", ydata=tdiff,
            inputdata=with_time_diff,
            plot_method=sns.pointplot, hue_col="input",
            row_col="version",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            palette=inputs_pallet, **pointplot_error_args
            )

"""
# I cant do this because speedup calculation already creates 
# a cross product and this gets to heavy 
with_speedup_diff, sdiff = relative_difference_to_list(with_speedup,
                                             column="speedup",
                                             eq_columns=["scenario", "version", "input"])

multi_plots(xdata="# independent functions", ydata=sdiff,
            inputdata=with_speedup_diff,
            plot_method=sns.pointplot, hue_col="input",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            palette=inputs_pallet, **pointplot_error_args
            )
""""""
# Plot Speedup only for smaller inputs
less_than_100 = with_speedup[with_speedup["input"] < 100]
multi_plots(xdata="# independent functions", ydata='speedup',
            inputdata=less_than_100,
            plot_method=sns.pointplot, hue_col="input",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            palette=inputs_pallet, **pointplot_error_args
            )

# Plot execution times compiled vs sequential for only one library
only_list_sum = only_seq_vs_comp[only_seq_vs_comp["library"] == "list_sum"]

multi_plots(xdata="# independent functions", ydata='time in ms',
            inputdata=only_list_sum, sharey=False, subTitle="library=list_sum",
            plot_method=sns.barplot, hue_col="version",
            column_col="input", col_order=[1, 10, 100, 1000],
            palette=versions_color_dict, **barplot_error_args
            )

multi_plots(xdata="# independent functions", ydata='time in ms',
            inputdata=only_seq_vs_comp, sharey=False,
            plot_method=sns.barplot, hue_col="version",
            column_col="input", col_order=[1, 10, 100, 1000],
            row_col="library",
            palette=versions_color_dict, **barplot_error_args
            )

# Plot execution times only for input 1000 but for all libraries
just1000 = only_seq_vs_comp[only_seq_vs_comp["input"] == 1000]
multi_plots(xdata="# independent functions", ydata='time in ms',
            inputdata=just1000, sharey=False, subTitle="input=1000",
            plot_method=sns.barplot, hue_col="library",
            column_col="version", col_order=["sequential", "compiled"],
            palette=lib_color_dict, **barplot_error_args
            )

# Plot execution times only for input 10 but for all libraries
just10 = only_seq_vs_comp[only_seq_vs_comp["input"] == 10]
multi_plots(xdata="# independent functions", ydata='time in ms',
            inputdata=just10, sharey=False, subTitle="input=10",
            plot_method=sns.barplot, hue_col="library",
            column_col="version", col_order=["sequential", "compiled"],
            **barplot_error_args
            )

# Plot relative Overhead
only_seq_vs_comp = natPar_df[
    (natPar_df["version"] == "sequential")
    | (natPar_df["version"] == "compiled")]
with_relative_overhead, overhead_column = \
    relative_overhead(only_seq_vs_comp, ["scenario", "version", "input"])
only_sequential = with_relative_overhead[
    with_relative_overhead["version"] == "sequential"]
only_compiled = with_relative_overhead[
    with_relative_overhead["version"] == "compiled"]
    
multi_plots(xdata="# independent functions", ydata=overhead_column,
            inputdata=only_sequential,
            plot_method=sns.barplot, hue_col="input",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            palette=inputs_pallet,
            **barplot_error_args
            )

multi_plots(xdata="# independent functions", ydata=overhead_column,
            inputdata=only_compiled,
            plot_method=sns.barplot, hue_col="input",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            palette=inputs_pallet,
            **barplot_error_args
            )
"""