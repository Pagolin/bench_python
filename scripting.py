import pandas as pd
import seaborn as sns
from scipy.stats.mstats import gmean

from df_utils import procs_from_scenario, df_with_speedup, \
    substract_parallel_overhead, add_speedup
from plotting import set_plus_minus, multi_plots

pd.set_option('display.max_columns', 16)

combined = pd.read_csv("./natPars_no_means.csv",
                       index_col=0)

combined["time in ms"] = combined["time"]
combined["# independent functions"] = procs_from_scenario(combined)
no_pass = combined[combined["library"] != "pass"]
in_data = no_pass[(no_pass["version"] == "sequential")
                  | (no_pass["version"] == "compiled")]

multi_plots(xdata="# independent functions", ydata='time', inputdata=in_data,
            plot_method=sns.barplot, hue_col="version",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            estimator=gmean, ci="sd", dodge=True, palette="Set2"
            )

with_speedup = add_speedup(no_pass, ["scenario", "library", "input"])

# Plot Speedup
multi_plots(xdata="# independent functions", ydata='speedup',
            inputdata=with_speedup,
            plot_method=sns.barplot, hue_col="version",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            estimator=gmean, ci="sd", dodge=True, palette="Set2"
            )

exit(0)
"""
# Plot execution times
multi_plots(xdata='# loops', ydata='time', inputdata=no_pass,
            plot_method=sns.barplot, hue_col="library",
            column_col="version", col_order=["sequential", "compiled"],
            estimator=gmean, ci="sd", dodge=True, palette="Set2"
            )

with_speedup = add_speedup(no_pass, ["scenario", "library", "input"])

# Plot Speedup
multi_plots(xdata='# loops', ydata='speedup', inputdata=with_speedup,
            plot_method=sns.barplot, hue_col="library",
            column_col="version",
            estimator=gmean, ci="sd", dodge=True, palette="Set2"
            )


combined["run_index"] = combined.index % 10
with_relative_overhead, overhead_column = realtive_overhead(combined, ["run_index", "version", "input"])
print(with_relative_overhead[with_relative_overhead["version"]=="sequential"])

multi_plots(xdata='# loops', ydata=overhead_column,
            inputdata=with_relative_overhead,
            plot_method=sns.barplot, hue_col="library",
            column_col="version",
            estimator=gmean, ci="sd", dodge=True, palette="Set2"
            )
            

versionsOfThree = no_pass[no_pass["# independent functions"] == 3]
versionsOfThree.sort_values(by="version", axis=0, inplace=True)
multi_plots(xdata="version", ydata="time in ms", inputdata=versionsOfThree,
            plot_method=sns.barplot, hue_col="input",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            estimator=gmean, ci="sd", dodge=True, palette="Set2"
            )

with_speedup= add_speedup(versionsOfThree,
                                   ["scenario", "library", "input"])
with_speedup.sort_values(by="version", axis=0, inplace=True)

multi_plots(xdata="version", ydata="speedup", inputdata=with_speedup,
            plot_method=sns.barplot, hue_col="input",
            column_col="library", col_order=["lists", "list_sum", "list_io"],
            estimator=gmean, ci="sd", dodge=True, palette="Set2"
            )


exit(0)
"""
"""


exit(0)

times_all, legend_col = make_legend_column(in_data, ["version", "input"])
times = times_all[times_all["input"] < 100]

set_plus_minus(times, "max", "geo-mean", "min")
multi_plots(inputdata=times, xdata="# independent functions", ydata="geo-mean",
            hue_col="version", column_col="library", yplus="max",
            set_x_ticks=True, yminus="min", palette="Set2", style="input")

times_1 = times_all[times_all["input"] == 1]

set_plus_minus(times_1, "max", "geo-mean", "min")
multi_plots(inputdata=times_1, xdata="# independent functions", ydata="geo-mean",
            hue_col=legend_col, column_col="library", yplus="max",
            yminus="min", palette="Set2")

"""
with_speedups, _ = df_with_speedup(in_data, ["scenario", "library", "input"])
with_speedups["# independent functions"] = procs_from_scenario(with_speedups)
with_speedups["processes"] = with_speedups["# independent functions"] + 1

set_plus_minus(with_speedups, y_max="S_max", y_mean="S_mean", y_min="S_min")
multi_plots(inputdata=with_speedups, xdata="# independent functions",
            ydata="S_mean",
            hue_col="input", column_col="library",
            col_order=["lists", "list_sum", "list_io"],
            yplus="y_plus",
            yminus="y_minus", palette="Set2")
without_overhead = \
    substract_parallel_overhead(combined,
                                eq_columns=["scenario", "version", "input"])

speedup_without_overhead, le = \
    df_with_speedup(without_overhead, ["scenario", "library", "input"])
set_plus_minus(speedup_without_overhead, y_max="S_max", y_mean="S_mean",
               y_min="S_min")

multi_plots(inputdata=speedup_without_overhead,
            xdata="# independent functions",
            ydata="S_mean", hue_col="input", column_col="library",
            col_order=["lists", "list_sum", "list_io"],
            set_x_ticks=True,
            yplus="y_plus", yminus="y_minus", palette="Set2")

versionsOfThree = no_pass[no_pass["# independent functions"] == 3]
# execution times plot
set_plus_minus(versionsOfThree, "max", "geo-mean", "min")

multi_plots(xdata="version", ydata="geo-mean", inputdata=versionsOfThree,
            hue_col="input", column_col="library", plot_method=
            sns.pointplot, join=False, dodge=0.2,
            col_order=["lists", "list_sum", "list_io"], palette="Set2")

with_speedup, le = df_with_speedup(versionsOfThree,
                                   ["scenario", "library", "input"])

set_plus_minus(with_speedup, y_max="S_max", y_mean="S_mean", y_min="S_min")
with_speedup.sort_values(by="version", axis=0, inplace=True)
multi_plots(xdata="version", ydata="S_mean", inputdata=with_speedup,
            hue_col="input", column_col="library", plot_method=
            sns.pointplot,
            col_order=["lists", "list_sum", "list_io"], dodge=0.2,
            palette="Set2", join=False)
