import pandas as pd
import seaborn as sns
from df_utils import procs_from_scenario, df_with_speedup, make_legend_column,\
    substract_parallel_overhead
from plotting import set_plus_minus, multi_plots

pd.set_option('display.max_columns', 16)

files = ["./measurements/list_sum_1_10_100.csv",
         "./measurements/lists_1_10_100.csv",
         "./measurements/pass_1_10_100.csv"]


combined = pd.read_csv("measurements/combined_all_as_milli.csv",
                       index_col=0)



no_pass = combined[combined["library"] != "pass"]
in_data = no_pass[(no_pass["version"] == 'sequential')
                   | (no_pass["version"] == "compiled")]

"""
with_speedups, _ = df_with_speedup(in_data, ["scenario", "library", "input"])
with_speedups["# independent functions"] = procs_from_scenario(with_speedups)
with_speedups["processes"] = with_speedups["# independent functions"] + 1

set_plus_minus(with_speedups, y_max="S_max", y_mean="S_mean", y_min="S_min")
multi_plots(with_speedups, xdata="# independent functions", ydata="S_mean",
            hue_col="input", column_col="library", yplus="y_plus",
            yminus="y_minus", palette="Set2")

times_all, legend_col = make_legend_column(in_data, ["version", "input"])
times = times_all[times_all["input"] == 10]

set_plus_minus(times, "max", "geo-mean", "min")
multi_plots(times, xdata="# independent functions", ydata="geo-mean",
            hue_col=legend_col, column_col="library", yplus="max",
            yminus="min", palette="Set2")

times_1 = times_all[times_all["input"] == 1]

set_plus_minus(times_1, "max", "geo-mean", "min")
multi_plots(times_1, xdata="# independent functions", ydata="geo-mean",
            hue_col=legend_col, column_col="library", yplus="max",
            yminus="min", palette="Set2")




without_overhead = \
    substract_parallel_overhead(combined,
                                eq_columns=["scenario", "version", "input"])

speedup_without_overhead, le = \
    df_with_speedup(without_overhead, ["scenario", "library", "input"])
set_plus_minus(speedup_without_overhead, y_max="S_max", y_mean="S_mean", y_min="S_min")

multi_plots(speedup_without_overhead, xdata="# independent functions",
            ydata="S_mean", hue_col="input", column_col="library",
            yplus="y_plus", yminus="y_minus", palette="Set2")

"""

versionsOfThree = no_pass[no_pass["# independent functions"] == 3]
# execution times plot
set_plus_minus(versionsOfThree, "max", "geo-mean", "min")
groups = versionsOfThree.groupby(["version", "library","input"]).count()

multi_plots(xdata="version", ydata="geo-mean", inputdata=versionsOfThree,
            hue_col="input", column_col="library", plot_method=
            sns.pointplot, join=False)

with_speedup, le  = df_with_speedup(versionsOfThree, ["scenario", "library", "input"])
groups = with_speedup.groupby(["version", "library","input"]).count()
print(groups)
set_plus_minus(with_speedup, y_max="S_max", y_mean="S_mean", y_min="S_min")
multi_plots(xdata="version", ydata="S_mean", inputdata=with_speedup,
            hue_col="input", column_col="library", plot_method=
            sns.scatterplot, palette="Set2")

exit(0)

