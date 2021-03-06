import os
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

def add_speedup(data, columns, time_col=None):
    basevalues = data[data.version == "sequential"]
    if not time_col:
        time_col = "time"
    # join dataframes such that every measurement
    # has the according sequential measurement in the same row
    same_data_row = columns

    compared_to_sequential = data.merge(
        basevalues,
        on=same_data_row,
        suffixes=('', '_seq'))

    # speedup = parallel time /sequential time
    compared_to_sequential["speedup"] = compared_to_sequential[time_col+"_seq"] \
                                       / compared_to_sequential[time_col]

    # Remove sequential results from speedup plot
    compared_to_sequential = compared_to_sequential[
        compared_to_sequential["version"] != "sequential"]
    return compared_to_sequential


def substract_overhead(input: pd.DataFrame, eq_columns: List[str]):
    data = input.copy(deep=True)
    times_for_pass = data[data["library"] == "pass"]
    compared_to_pass = data.merge(times_for_pass, on=eq_columns,
                                  suffixes=('', '_pass'))
    compared_to_pass["time"] = compared_to_pass["time"] \
                                      - compared_to_pass["time_pass"]
    # Remove the pass measures
    result = compared_to_pass[compared_to_pass["library"] != "pass"]
    return result

def relative_overhead(input: pd.DataFrame, eq_columns: List[str]):
    data = input.copy(deep=True)
    times_for_pass = data[data["library"] == "pass"]
    overhead_column = "overhead in %"
    compared_to_pass = data.merge(times_for_pass, on=eq_columns,
                                  suffixes=('', '_pass'))
    compared_to_pass[overhead_column] = compared_to_pass["time_pass"] \
                                        / compared_to_pass["time"] * 100
    # Remove the pass measures
    result = compared_to_pass[compared_to_pass["library"] != "pass"]
    return result, overhead_column

def make_legend_column(df, columns):
    joined_name = "_".join(columns)
    join_func = lambda series: "_".join(map(str, series.values))
    df[joined_name] = df[
        columns].aggregate(join_func, axis="columns")
    return df, joined_name


def accumulate_files(data_dir, base_file, pattern):
    accumulate_df = pd.read_csv(data_dir + base_file, index_col=0)

    for file in os.listdir(data_dir):
        filename = os.fsdecode(file)
        if pattern in filename and filename != base_file:
            current_df = pd.read_csv(data_dir + filename, index_col=0)
            accumulate_df = accumulate_df.append(current_df, ignore_index=True)

    accumulate_df["time in ms"] = accumulate_df["time"]
    accumulate_df = accumulate_df.drop("reps", axis=1)
    return accumulate_df


def relative_to_list(input: pd.DataFrame, column, eq_columns: List[str]):
    data = input.copy(deep=True)
    scale_to_avoid_undeflow = 100
    list_values = data[data["library"] == "lists"]
    difference_column = "{} difference in %".format(column)
    compared_to_list = data.merge(list_values, on=eq_columns,
                                  suffixes=('', '_list'))
    compared_to_list[difference_column] = compared_to_list[column] \
                                        / compared_to_list[column+"_list"] * 100

    return compared_to_list, difference_column