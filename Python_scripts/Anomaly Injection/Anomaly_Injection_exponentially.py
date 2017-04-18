#inject anomalies exponentially
def add_anomaly_exp(num):
    t_num = make_zeroes(num)
    num.sort()
    mu = len(num)/2
    print mu
    last_idx = len(num) - 1
    #print last_idx
    for j in range(0,len(num)):
        if j <= mu:
            #print j
            t_num[j] = num[j] * math.exp(float(j)/float(mu)) - j * (float(num[j])/float(mu))
            #t_num[j] = num[j] * (num[mu] ** j)
        else:
            k = last_idx - j
            #t_num[j] = num[j] * (num[mu] ** k)
            t_num[j] = num[j] * math.exp(float(k)/float(mu)) - k * (float(num[j])/float(mu))
    return t_num 
