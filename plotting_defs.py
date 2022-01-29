import seaborn as sns
from scipy.stats.mstats import gmean

sns.set_style("darkgrid")

# Some color paletts
inputs_pallet = "Blues_d"
relations_pallet = "YlOrRd"
block_size_pallet = "YlGnBu"

colors = sns.color_palette("Set2")
versions_color_dict = {"sequential": colors[1], "compiled": colors[0],
                       "pooled": colors[2], "threaded": colors[3]}

lib_colors = sns.color_palette("tab10")
lib_color_dict = {"lists": lib_colors[3], "list_sum": lib_colors[1],
                  "list_io": lib_colors[0]}

pallet_selector = {"input": inputs_pallet, "library": lib_color_dict,
                   "version": versions_color_dict,
                   "relation": relations_pallet,
                   "case block size":block_size_pallet}


# Some default args for my plots
barplot_error_args = {"estimator": gmean, "ci": "sd",
                      "errwidth": 1.0, "errcolor": "slategray", "capsize": 0.1}
pointplot_error_args = {"estimator": gmean, "ci": "sd", "dodge": 0.4,
                        "join": False,
                        "scale": 0.6, "errwidth": 1.3, "capsize": 0.08, }


data_dir = "../remoteMeasures/"
natPars = "natParMeasures_Shakespeare.csv"
pipelines_old = "pipelineMeasures_Shakespeare.csv"
branching_old = "branchingMeasures_Shakespeare.csv"
pipelines = "pipelineMeasures_Shakespeare_NEW.csv"
branching = "branchingMeasures_Shakespeare_NEW.csv"