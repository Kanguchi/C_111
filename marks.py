import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()
mean = statistics.mean(df["Math_score"])
dev = statistics.stdev(df["Math_score"])
# find standard deviations

math_scores1 = pd.read_csv("data1.csv")["Math_score"].tolist()
math_scores2 = pd.read_csv("data2.csv")["Math_score"].tolist()
math_scores3 = pd.read_csv("data3.csv")["Math_score"].tolist()

mean1 = statistics.mean(math_scores1)
mean2 = statistics.mean(math_scores2)
mean3 = statistics.mean(math_scores3)


def showfig(lst):
    df = lst
    mean = statistics.mean(df)
    dev = statistics.stdev(df)
    dev1_strt, dev1_end = mean - dev, mean + dev
    dev2_strt, dev2_end = mean - 2*dev, mean + 2*dev
    dev3_strt, dev3_end = mean - 3*dev, mean + 3*dev
    fig = ff.create_distplot([df], ["Math Scores"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode="lines", name = "MEAN"))
    fig.add_trace(go.Scatter(x = [dev1_strt, dev1_strt], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 START"))
    fig.add_trace(go.Scatter(x = [dev1_end, dev1_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
    fig.add_trace(go.Scatter(x = [dev2_strt, dev2_strt], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 START"))
    fig.add_trace(go.Scatter(x = [dev2_end, dev2_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
    fig.add_trace(go.Scatter(x = [dev3_strt, dev3_strt], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 START"))
    fig.add_trace(go.Scatter(x = [dev3_end, dev3_end], y = [0, 0.17], mode = "lines", name = "STANDARD DEVIATION 3 END")) 
    fig.add_trace(go.Scatter(x = [mean1, mean1], y = [0, 0.15], mode = "lines", name = "MEAN OF GROUP1"))   
    fig.add_trace(go.Scatter(x = [mean2, mean2], y = [0, 0.15], mode = "lines", name = "MEAN OF GROUP2"))   
    fig.add_trace(go.Scatter(x = [mean3, mean3], y = [0, 0.15], mode = "lines", name = "MEAN OF GROUP3"))   
    fig.show()
    print(mean)
    print(dev)
    # fig.show()

def randomsetofmean(counter):
    ds = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        # print(random_index)
        value = data[random_index]
        ds.append(value)
    mean = statistics.mean(ds)
    return mean

def setup():
    meanlist = []
    for i in range(0, 100):
        setofmean = randomsetofmean(100)
        meanlist.append(setofmean)
    showfig(meanlist)

setup()
print(mean)
print(std_dev)
