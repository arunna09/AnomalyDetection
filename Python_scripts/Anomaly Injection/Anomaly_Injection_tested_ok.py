#created on 27.03.2017 by Arun Kumar N A
#To inject anomaly which gradually increases 
#mean = data point selected for injecting anomaly
#length = the number of points considered along both sides of the selected data point
#increment = by how much to increase which is user defined while injecting anomaly
#returns the array after injecting anomaly

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

sample_data = [100] * 9
sample_random_data = [952, 335, 216, 912, 732, 777, 139, 176, 215, 99]
anomaly_data = add_anomaly(sample_random_data,50.0)
anomaly1_data = add_anomaly(sample_data,10.0)
