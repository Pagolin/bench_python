from typing import List

import pandas as pd


def procs_from_scenario(df: pd.DataFrame):
    newcol = []
    for sc in df["scenario"]:
        nums = [b for b in list(sc) if b.isdigit()]
        num = int(''.join(nums))
        newcol.append(num)
    return newcol


def df_with_speedup(data, columns):
    basevalues = data[data.version == "sequential"]

    # join dataframes such that every measurement
    # has the according sequential measurement in the same row
    same_data_row = columns

    compared_to_sequential = data.merge(
        basevalues,
        on=same_data_row,
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
    compared_to_sequential = compared_to_sequential[
        compared_to_sequential["version"] != "sequential"]

    # Make one column for hue
    cjoin = lambda x: "_".join(map(str, x.values))
    legen_item = "_".join(columns)

    compared_to_sequential[legen_item] = compared_to_sequential[
        columns].aggregate(cjoin, axis="columns")

    compared_to_sequential.sort_values(by=legen_item, axis=0, inplace=True)
    compared_to_sequential.sort_values(by="scenario", axis=0, inplace=True)
    return compared_to_sequential, legen_item


def substract_parallel_overhead(input: pd.DataFrame, eq_columns: List[str]):
    data = input.copy(deep=True)
    times_for_pass = data[data["library"] == "pass"]
    compared_to_pass = data.merge(times_for_pass, on=eq_columns,
                                  suffixes=('', '_pass'))
    compared_to_pass["min"] = compared_to_pass["min"] \
                                      - compared_to_pass["min_pass"]
    compared_to_pass["geo-mean"] = compared_to_pass["geo-mean"] \
                                      - compared_to_pass["geo-mean_pass"]
    compared_to_pass["max"] = compared_to_pass["max"] \
                                       - compared_to_pass["max_pass"]
    # Remove the pass measures
    result = compared_to_pass[compared_to_pass["library"] != "pass"]
    return result


def make_legend_column(df, columns):
    joined_name = "_".join(columns)
    join_func = lambda series: "_".join(map(str, series.values))
    df[joined_name] = df[
        columns].aggregate(join_func, axis="columns")
    return df, joined_name
