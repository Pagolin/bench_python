import pandas as pd

columns = ["scenario","version","library","input","reps","min","geo-mean","max"]
data = []
for i in range(1,5):
    s = "test{}".format(i), "sequential", "lib", 5, 20, 2*i + (i-1)*0.5 , 3*i + (i-1)*0.5, 4*i+ (i-1)*0.5
    c = "test{}".format(i), "compiled", "lib", 5, 20, 1*i, 1.5*i, 2*i
    c_better =  "test{}".format(i), "optimal", "lib", 5, 20, 1*(i*0.5), 1.5*(i*0.5), 2*(i*0.5)
    data.append(s)
    data.append(c)
    data.append(c_better)
testDf = pd.DataFrame(columns=columns, data=data)
testDf.to_csv("./test_csv")