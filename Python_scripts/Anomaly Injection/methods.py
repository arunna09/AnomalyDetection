#create an empty list containing all zero values with similar size of the selected distribution
def make_zeroes(n):
    m = []
    for i in iter(n):
        m.append(0)
    return m

#changed values until mean of the selected distribution
def add_anomaly(num):
    t_num = make_zeroes(num)
    num.sort()
    mean = np.mean(num)
    diff = mean
    for j in iter(num):
        if j == mean:
            t_num[num.index(j)] = mean + diff
        elif j < mean:
            t_num[num.index(j)] = num[num.index(j)] + (num[num.index(j)] - num[0])
        else :
            t_num[num.index(j)] = num[num.index(j)]
    return t_num

#Added positive anomalies which increases untill mean value and decreases after mean value
#Change the value of diff based on the precision level you want your model to detect.
def add_anomaly_2(num):
    t_num = make_zeroes(num)
    num.sort()
    mean = np.mean(num)
    diff = mean
    for k in iter(num):
        if k == mean:
            t_num[num.index(k)] = mean + diff
        elif k < mean:
            t_num[num.index(k)] = num[num.index(k)] + (diff * (1 - ( (mean - num[num.index(k)]) / (mean - num[0]) )))
        else:
            t_num[num.index(k)] = num[num.index(k)] + (diff * (1 - ( (mean - num[num.index(k)]) / (mean - num[-1]) )))
    return t_num

#Added negative anomalies which increases untill mean value and decreases after mean value
def add_anomaly_3(num):
    t_num = make_zeroes(num)
    num.sort()
    mean = np.mean(num)
    diff = 2 * mean
    for k in iter(num):
        if k == mean:
            t_num[num.index(k)] = mean - diff
        elif k < mean:
            t_num[num.index(k)] = num[num.index(k)] - (diff * (1 - ( (mean - num[num.index(k)]) / (mean - num[0]) )))
        else:
            t_num[num.index(k)] = num[num.index(k)] - (diff * (1 - ( (mean - num[num.index(k)]) / (mean - num[-1]) )))
            #t_num[num.index(k)] = num[num.index(k)]
    return t_num
