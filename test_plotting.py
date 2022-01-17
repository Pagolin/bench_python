import pandas as pd

from plotting import set_plus_minus, multi_plots

columns = ["scenario", "version", "library", "input", "reps", "min",
           "geo-mean", "max"]
data = []
min_lib = 0.1
average_lib = 0.2
max_lib = 0.2
par_factor_lib = 0.6  # i.e. 2 parallel functions yield a speedup of 1.2

min_lib_other = 0.05
average_lib_other = 0.2
max_lib_other = 0.2
par_factor_lib_other = 0.7

for j in [3, 7, 15, 31]:
    s10 = j, "sequential", "lib", 10, 10, \
          j * 10 * min_lib, \
          j * 10 * average_lib, \
          j * 10 * max_lib
    c10 = j, "compiled", "lib", 10, 10, \
          (j * par_factor_lib) * 10 * min_lib, \
          (j * par_factor_lib) * 10 * average_lib, \
          (j * par_factor_lib) * 10 * max_lib
    data.append(s10)
    data.append(c10)
    s20 = j, "sequential", "lib", 20, 10, \
          j * 20 * min_lib, \
          j * 20 * average_lib, \
          j * 20 * max_lib
    c20 = j, "compiled", "lib", 20, 10, \
          (j * par_factor_lib) * 20 * min_lib, \
          (j * par_factor_lib) * 20 * average_lib, \
          (j * par_factor_lib) * 20 * max_lib
    data.append(s20)
    data.append(c20)
    s10 = j, "sequential", "lib_other", 10, 10, \
          j * 10 * min_lib_other, \
          j * 10 * average_lib_other, \
          j * 10 * max_lib_other
    c10 = j, "compiled", "lib_other", 10, 10, \
          (j * par_factor_lib_other) * 10 * min_lib_other, \
          (j * par_factor_lib_other) * 10 * average_lib_other, \
          (j * par_factor_lib_other) * 10 * max_lib_other
    data.append(s10)
    data.append(c10)
    s20 = j, "sequential", "lib_other", 20, 10, \
          j * 20 * min_lib_other, \
          j * 20 * average_lib_other, \
          j * 20 * max_lib_other
    c20 = j, "compiled", "lib_other", 20, 10, \
          (j * par_factor_lib_other) * 20 * min_lib_other, \
          (j * par_factor_lib_other) * 20 * average_lib_other, \
          (j * par_factor_lib_other) * 20 * max_lib_other
    data.append(s20)
    data.append(c20)

testDf = pd.DataFrame(columns=columns, data=data)
testDf.to_csv("./test_csv")


testDf = pd.read_csv("test_csv", index_col=0)
set_plus_minus(testDf, "max", "geo-mean", "min")
testDf["# independent functions"] = testDf['scenario']
multi_plots(xdata="# independent functions", ydata="geo-mean",
            inputdata=testDf, plot_method=sn.scatterplot, hue_col="input",
            column_col="library", yplus="y_plus", yminus="y_minus")

