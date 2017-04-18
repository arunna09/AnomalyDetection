#inject anomaly from start point to endpoint
def add_anomaly(num,x):
    t_num = make_zeroes(num)
    num.sort()
    #mean = np.mean(num)
    mu = len(num)/2 
    last_idx = len(num)
    delta = 1.0 + (x/100)
    for j in range(0,len(num)):
        increment = num[mu] * delta
        if j == mu:
            t_num[j] = increment
        else:
            increment_new = increment - num[mu]
            share = abs(mu - j)
            t_num[j] = num[j] + increment_new * (1.0 - (float(share)/float(mu)))
    return t_num 
