from plotting import *

branching_df = pd.read_csv(data_dir + branching, index_col=0)
branching_df["input length"] = branching_df["# loops"]

basecases = branching_df[
    ((branching_df["value"] == 2) &
        (branching_df["modified function"] != "case block size ")) |
    ((branching_df["value"] == 1) &
        (branching_df["modified function"] == "case block size "))]\
    .copy(deep=True)

all_relational = branching_df[
    branching_df["modified function"] != "case block size "].copy(deep=True)
check_function_experiments = branching_df[
    branching_df["modified function"] == "check relation"].copy(deep=True)
branch_function_experiments = branching_df[
    branching_df["modified function"] == "branch time relation"].copy(
    deep=True)
input_blocks_experiments = branching_df[
    branching_df["modified function"] == "case block size "].copy(deep=True)
input_case_distribution_experiments = branching_df[
    branching_df["modified function"] == "case distribution"].copy(deep=True)


def val_to_rel(val):
    relation_from_value = {2: "1:1", 3: "1:2", 5: "1:4", 9: "1:8", 1: "1:0"}
    return relation_from_value[val]


# Rename interesting columns
check_function_experiments["relation if:else"] = \
    check_function_experiments["value"].apply(val_to_rel)

branch_function_experiments["input relation if_fun:else_fun"] = \
    branch_function_experiments["value"].apply(val_to_rel)

input_blocks_experiments["case block size"] = \
    input_blocks_experiments["value"]

input_case_distribution_experiments["case distributions"] = \
    input_case_distribution_experiments["value"].apply(val_to_rel)

all_relational["relation"] = all_relational["value"].apply(val_to_rel)

# Plot execution times / speedups
# Check experiment
multi_plots(xdata="input length", ydata='time in ms',
            inputdata=check_function_experiments,
            plot_method=sns.barplot, hue_col="relation if:else",
            column_col="version", col_order=["sequential", "compiled"],
            **barplot_error_args
            )
speedup_check_experiments = add_speedup(check_function_experiments,
                                        ["input length", "value"])

multi_plots(xdata="input length", ydata='speedup',
            inputdata=speedup_check_experiments,
            plot_method=sns.barplot, hue_col="relation if:else",
            column_col="modified function",
            **barplot_error_args
            )

# Costs of branch functions experiment
multi_plots(xdata="input length", ydata='time in ms',
            inputdata=branch_function_experiments,
            plot_method=sns.barplot, hue_col="input relation if_fun:else_fun",
            column_col="version", col_order=["sequential", "compiled"],
            **barplot_error_args
            )

speedup_branch_experiments = add_speedup(branch_function_experiments,
                                         ["input length", "value"])

multi_plots(xdata="input length", ydata='speedup',
            inputdata=speedup_branch_experiments,
            plot_method=sns.barplot, hue_col="input relation if_fun:else_fun",
            column_col="modified function",
            **barplot_error_args
            )

# Input block size experiment
multi_plots(xdata="input length", ydata='time in ms',
            inputdata=input_blocks_experiments,
            plot_method=sns.barplot, hue_col="case block size",
            column_col="version", col_order=["sequential", "compiled"],
            **barplot_error_args
            )

speedup_blocks_experiment = add_speedup(input_blocks_experiments,
                                        ["input length", "value"])

multi_plots(xdata="input length", ydata='speedup',
            inputdata=speedup_blocks_experiment,
            plot_method=sns.barplot, hue_col="case block size",
            column_col="modified function",
            **barplot_error_args
            )

# Input case distribution experiment
multi_plots(xdata="input length", ydata='time in ms',
            inputdata=input_case_distribution_experiments,
            plot_method=sns.barplot, hue_col="case distributions",
            column_col="version", col_order=["sequential", "compiled"],
            **barplot_error_args
            )

speedup_case_distribution_experiment = \
    add_speedup(input_case_distribution_experiments, ["input length", "value"])

multi_plots(xdata="input length", ydata='speedup',
            inputdata=speedup_case_distribution_experiment,
            plot_method=sns.barplot, hue_col="case distributions",
            column_col="modified function",
            **barplot_error_args
            )

# Are basecases of either experiment equally fast ?
multi_plots(xdata="input length", ydata='time in ms',
            inputdata=basecases, subTitle="Basecases",
            plot_method=sns.barplot, hue_col="modified function",
            column_col="version", col_order=["sequential", "compiled"],
            **barplot_error_args
            )

speedup_base_cases = add_speedup(basecases,
                                 ["input length", "modified function", "value"])

multi_plots(xdata="input length", ydata='speedup',
            inputdata=speedup_base_cases, subTitle="Basecases",
            plot_method=sns.barplot, hue_col="modified function",
            column_col="version", col_order=["compiled"],
            **barplot_error_args
            )

# Plot all relational modifications together
all_relational["time in ms per loop"] = all_relational["time"]/all_relational["# loops"]
sequential_relational = all_relational[all_relational["version"] == "sequential"]
compiled_relational = all_relational[all_relational["version"] == "compiled"]
multi_plots(xdata="input length", ydata="time in ms per loop",
            inputdata=all_relational,
            plot_method=sns.barplot, hue_col="relation",
            column_col="modified function",
            row_col = "version", margin_titles=True,
            **barplot_error_args
            )

multi_plots(xdata="input length", ydata="time in ms per loop",
            inputdata=compiled_relational,
            plot_method=sns.barplot, hue_col="relation",
            column_col="modified function",
            **barplot_error_args
            )

speedup_all_relational = add_speedup(all_relational,
                                     ["input length", "modified function", "value"])

multi_plots(xdata="input length", ydata='speedup',
            inputdata=speedup_all_relational,
            plot_method=sns.barplot, hue_col="relation",
            column_col="modified function",
            **barplot_error_args
            )

only1 = speedup_all_relational[speedup_all_relational["input length"] == 1]
groups = only1.groupby(["input length", "modified function", "value"]).agg({"speedup":["min", "mean", "max"]})
print(groups.head(20))

only1 = speedup_all_relational[speedup_all_relational["input length"] == 10]
groups = only1.groupby(["input length", "modified function", "value"]).agg({"speedup":["min", "mean", "max"]})
print(groups.head(20))

only1 = speedup_all_relational[speedup_all_relational["input length"] == 100]
groups = only1.groupby(["input length", "modified function", "value"]).agg({"speedup":["min", "mean", "max"]})
print(groups.head(20))

only1 = speedup_all_relational[speedup_all_relational["input length"] == 1000]
groups = only1.groupby(["input length", "modified function", "value"]).agg({"speedup":["min", "mean", "max"]})
print(groups.head(20))
