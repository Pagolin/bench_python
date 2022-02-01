#from plotting import *
import pandas as pd

no_gc = pd.read_csv("./gc_disabled_natPar4.csv", index_col=0)
gc_on = pd.read_csv("./gc_enabled_natPar4.csv", index_col=0)
merged = no_gc.merge(
    gc_on,
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