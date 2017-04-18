import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
%matplotlib inline

class plot_func():
    def __init__(self, x, clr, name):
        fig = plt.figure(1)
        ax = fig.add_subplot(111)
        ax.plot(x,color=clr,label=name)
        ax.legend(loc='upper right')
        ax.set_xbound(0,10)
        ax.set_ybound(1,100)
        ax.set_xlabel('Number of elements')
        ax.set_ylabel('Value')


def make_zeroes(n):
    m = []
    for i in iter(n):
        m.append(0)
    return m

def add_anomaly(num):
    t_num = make_zeroes(num)
    num.sort()
    mean = np.mean(num)
    for j in iter(num):
        if j == mean:
            t_num[num.index(j)] = mean + mean
        elif j < mean:
            t_num[num.index(j)] = num[num.index(j)] + (num[num.index(j)] - num[0])
        else :
            t_num[num.index(j)] = num[num.index(j)]
    return t_num  

sample_data = [10,20,30,40,50,60,70,80,90]
anomaly_data = add_anomaly(sample_data)

test1 = plot_func(sample_data,'red','Original')
test2 = plot_func(anomaly_data,'blue','Anomaly') 
