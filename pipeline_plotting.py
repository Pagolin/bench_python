from scripting import *

pipeline_df = pd.read_csv(data_dir + pipelines, index_col=0)
no_pass = pipeline_df[pipeline_df["library"] != "pass"]
with_speedup = add_speedup(no_pass, ["scenario", "library", "input"])

# Plot execution time
multi_plots(xdata="# loops", ydata='time in ms',
            inputdata=no_pass,
            plot_method=sns.barplot, hue_col="library",
            column_col="version", col_order=["sequential", "compiled"],
            **barplot_error_args
            )

# Plot execution time per loop
no_pass["time per loop in ms"] = no_pass["time"]/no_pass["# loops"]
multi_plots(xdata="# loops", ydata="time per loop in ms",
            inputdata=no_pass,
            plot_method=sns.barplot, hue_col="library",
            column_col="version", col_order=["sequential", "compiled"],
            **barplot_error_args
            )

# Plot Speedup
multi_plots(xdata="# loops", ydata='speedup',
            inputdata=with_speedup,
            plot_method=sns.pointplot, hue_col="library",
            column_col="version",
            **pointplot_error_args
            )
# Compare Speedup old version vs new version:
multi_plots(xdata="# loops", ydata='speedup',
            inputdata=with_speedup,subTitle="Input used",
            plot_method=sns.pointplot, hue_col="library",
            column_col="version",
            **pointplot_error_args
            )

pipeline_df_old = pd.read_csv(data_dir + pipelines_old, index_col=0)
no_pass_old = pipeline_df_old[pipeline_df_old["library"] != "pass"]
with_speedup_old = add_speedup(no_pass_old, ["scenario", "library", "input"])
multi_plots(xdata="# loops", ydata='speedup',
            inputdata=with_speedup_old,subTitle="Input not used",
            plot_method=sns.pointplot, hue_col="library",
            column_col="version",
            **pointplot_error_args
            )

no_pass_old["time per loop in ms"] = no_pass_old["time"]/no_pass_old["# loops"]
multi_plots(xdata="# loops", ydata='time in ms',
            inputdata=no_pass_old,subTitle="Input not used",
            plot_method=sns.barplot, hue_col="library",
            column_col="version", col_order=["sequential", "compiled"],
            **barplot_error_args
            )


# Plot Speedup per Loop
with_speedup_per_loop = add_speedup(no_pass, ["scenario", "library", "input"],
                                    time_col="time per loop in ms")
# -> skipped: for obvious Reasons it's just the same as the Speedup per run

# Plot relative overhead
with_relative_overhead, overhead_column = \
    relative_overhead(pipeline_df, ["scenario", "version", "input"])

multi_plots(xdata="# loops", ydata=overhead_column,
            inputdata=with_relative_overhead, sharey=False,
            plot_method=sns.barplot, hue_col="library",
            column_col="version", col_order=["sequential", "compiled"],
            **barplot_error_args
            )

