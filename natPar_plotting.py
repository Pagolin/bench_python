from scripting import *

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


# Assume  combine function took as long as the others
# (this underestimates perfect speedup)
# -> perfect speedup = all functions sequential/ tasks parallel + combine
# -> perfect speedup = #independent functions + 1 / 2

def perfect_speedup(num_cores, num_funs):
    return num_funs if num_funs <= num_cores else num_cores


with_speedup["perfect speedup"] = with_speedup[
    "# independent functions"].apply(lambda n: perfect_speedup(24, n))

with_speedup["% of perfect speedup"] = with_speedup["speedup"] \
                                       / with_speedup["perfect speedup"] \
                                       * 100
multi_plots(xdata="# independent functions", ydata="% of perfect speedup",
            inputdata=with_speedup,
            plot_method=sns.pointplot, hue_col="input",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            palette=inputs_pallet, **pointplot_error_args
            )

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
