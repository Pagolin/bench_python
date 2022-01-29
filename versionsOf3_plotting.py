from scripting import *

natPar_df = pd.read_csv(data_dir + natPars, index_col=0)
only_scenario_4 = natPar_df[natPar_df["# independent functions"] == 4]
no_pass = only_scenario_4[only_scenario_4["library"] != "pass"]

# Plot execution times
multi_plots(xdata="version", ydata='time in ms',
            inputdata=only_scenario_4,
            plot_method=sns.barplot, hue_col="input", rotate_labels=True,
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            palette=inputs_pallet, **barplot_error_args
            )
# Plot execution times pivot and leave out input 1000
without1000 = only_scenario_4[only_scenario_4["input"] < 1000]
multi_plots(xdata="version", ydata='time in ms',
            inputdata=without1000,
            plot_method=sns.barplot, hue_col="input", rotate_labels=True,
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            **barplot_error_args
            )
multi_plots(xdata="input", ydata='time in ms',
            inputdata=without1000,
            plot_method=sns.barplot, hue_col="version",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            **barplot_error_args
            )
# Plot Speedup
with_speedup = add_speedup(only_scenario_4, ["library", "input"])
multi_plots(xdata="input", ydata='speedup',
            inputdata=with_speedup,
            plot_method=sns.barplot, hue_col="version",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            **barplot_error_args
            )

# Plot relative overhead
with_relative_overhead, overhead_column = \
    relative_overhead(only_scenario_4, ["scenario", "version", "input"])

multi_plots(xdata="input", ydata=overhead_column,
            inputdata=with_relative_overhead, sharey=False,
            plot_method=sns.barplot, hue_col="library",
            column_col="version",
            col_order=["sequential", "threaded", "compiled", "pooled"],
            **barplot_error_args
            )
