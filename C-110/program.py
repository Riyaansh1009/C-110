import statistics
import plotly.figure_factory as ff 
import pandas as pd 
import random

df = pd.read_csv("data.csv")
temp = df["temp"].tolist()

pop_mean = statistics.mean(temp)
stDev = statistics.stdev(temp)
print(stDev)
print(pop_mean)

# graph = ff.create_distplot([temp],["temperature"], show_hist= False)
# graph.show()

# list2 = []
# for i in range(0,100):
#     index = random.randint(0,len(temp))
#     value = temp[index]
#     list2.append(value)
# samplemean = statistics.mean(list2)
# samplestdev = statistics.stdev(list2)
# print(samplestdev)
# print(samplemean)

