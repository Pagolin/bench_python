from plotting import *
import pandas as pd

natPars_local = pd.read_csv("./local_natPars_noGC_1_10_100.csv", index_col=0)
natPars_df = pd.read_csv(data_dir+natPars, index_col=0)
changed_order = pd.read_csv(data_dir+"natPar32_changed_task_order.csv", index_col=0)

natPars_df_32_10 = natPars_df[(natPars_df["# independent functions"]==32)
                              & (natPars_df["input"]==10)]
natPars_df_32_10["order"] = "original"
changed_order["order"] = "changed"
both = natPars_df_32_10.append(changed_order, ignore_index=True)
no_pass = both[both["library"] != "pass"]
with_speedup = add_speedup(no_pass, ["scenario", "library", "input", "order"])
multi_plots(xdata="library", ydata='speedup',
            inputdata=with_speedup,column_col="version",
            plot_method=sns.pointplot, hue_col="order",
            **pointplot_error_args
            )
multi_plots(xdata="library", ydata="time in ms", inputdata=no_pass,
            column_col="order", hue_col="version",
            plot_method=sns.barplot, **barplot_error_args)

exit(0)
gc_measures_dir = "/home/lisza/measures_with_gc/"

no_gc = pd.read_csv(data_dir + "natParMeasures_Shakespeare.csv" , index_col=0)

tasks4_no_gc = no_gc[no_gc["# independent functions"]==4]
tasks4_no_gc["gc_ebabled"] = False
gc_on = pd.read_csv(gc_measures_dir
                    + "time_measures_natPar4_2022_02_01_03_29.csv", index_col=0)

gc_on["time in ms"] = gc_on["time"]
gc_on = gc_on.drop("reps", axis=1)
gc_on["# independent functions"] = procs_from_scenario(gc_on)

merged = no_gc.merge(
    tasks4_no_gc,
    on=["scenario","version","library","input"],
    suffixes=('_off', '_on'))

merged["difference"] =  merged["time_on"] - merged["time_off"]
merged["% difference"] = merged["difference"]/ merged["time_off"] * 100

# print(merged[["scenario","version","library","input","% difference"]].head(20))

groups = merged.groupby(["scenario","version","library","input"]).agg({"% difference":['min', 'mean', 'max']})

print(groups.head(50))

print('###########################################\n')
gc_on_2 = pd.read_csv("./gc_enabled_natPar4_2.csv", index_col=0)
merged = no_gc.merge(
    gc_on_2,
    on=["scenario","version","library","input"],
    suffixes=('_off', '_on'))

merged["difference"] =  merged["time_on"] - merged["time_off"]
merged["% difference"] = merged["difference"]/ merged["time_off"] * 100

# print(merged[["scenario","version","library","input","% difference"]].head(20))

groups = merged.groupby(["scenario","version","library","input"]).agg({"% difference":['min', 'mean', 'max']})
print(groups.head(50))