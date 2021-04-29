import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("School1.csv")
data = df["Math_score"].tolist()
mean = statistics.mean(df["Math_score"])
dev = statistics.stdev(df["Math_score"])
# find standard deviations

school1 = pd.read_csv("School1.csv")["Math_score"].tolist()
school2 = pd.read_csv("School2.csv")["Math_score"].tolist()
school3 = pd.read_csv("School3.csv")["Math_score"].tolist()

sample1 = pd.read_csv("School_1_Sample.csv")["Math_score"].tolist()
sample2 = pd.read_csv("School_2_Sample.csv")["Math_score"].tolist()
sample3 = pd.read_csv("School_3_Sample.csv")["Math_score"].tolist()

mean1 = statistics.mean(sample1)
dev1 = statistics.stdev(sample1)
mean2 = statistics.mean(sample2)
print(mean2)
dev2 = statistics.stdev(school2)
mean3 = statistics.mean(sample3)
dev3 = statistics.stdev(school3)

def showfig(lst, school):
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
    if school == school1:
        fig.add_trace(go.Scatter(x = [mean1, mean1], y = [0, 0.15], mode = "lines", name = "MEAN OF School1")) 
        print(mean1)
        print(dev)
        print(f"The z score for school 1 is:{(mean1 - mean)/dev}")
    elif school == school2:
        fig.add_trace(go.Scatter(x = [mean2, mean2], y = [0, 0.15], mode = "lines", name = "MEAN OF School2"))
        print(mean2)
        print(f"The z score for school 2 is:{(mean2 - mean)/dev}")
    elif school == school3:
        fig.add_trace(go.Scatter(x = [mean3, mean3], y = [0, 0.15], mode = "lines", name = "MEAN OF School3"))
        print(mean3)
        print(f"The z score for school 3 is:{(mean3 - mean)/dev}")

    fig.show()
    # fig.show()

def randomsetofmean(counter, school):
    ds = []
    for i in range(0, counter):
        random_index = random.randint(0, len(school)-1)
        # print(random_index)
        value = school[random_index]
        ds.append(value)
    mean = statistics.mean(ds)
    return mean

def setup(school):
    meanlist = []
    for i in range(0, 100):
        setofmean = randomsetofmean(100, school)
        meanlist.append(setofmean)
    showfig(meanlist, school)

setup(school1)
setup(school2)
setup(school3)

