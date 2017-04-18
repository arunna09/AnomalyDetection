def make_zeroes(n):
    m = []
    for i in iter(n):
        m.append(0)
    return m

class plot_func():
    def __init__(self, data, clr, name):
        fig = plt.figure(1)
        ax = fig.add_subplot(111)
        ax.plot(range(1,len(data)+1),data,color=clr,label=name)
        ax.legend(loc='upper left')
        #ax.set_xbound(-1,10)
        #ax.set_ybound(1,100)
        ax.set_xlabel('Number of elements')
        ax.set_ylabel('Value')

if __name__ == "__main__":
    sample_data = [100] * 9
    sample_random_data = [952, 335, 216, 912, 732, 777, 139, 176, 215, 99, 480]
    anomaly_data = add_anomaly(sample_random_data,300.0)
    anomaly1_data = add_anomaly(sample_data,10.0)
    anomaly2_data = add_anomaly_exp(sample_data)
    anomaly3_data = add_anomaly_exp(sample_random_data)
    anomaly4_data = add_anomaly_dynamically(sample_data,40.0, 3, 5)
    anomaly5_data = add_anomaly_dynamically(sample_random_data, 40.0, 3, 5)
    
    test_1 = plot_func(sample_data,'red','Original Data')
    test_2 = plot_func(anomaly1_data,'blue','Anomalous Data')
    
    test3 = plot_func(sample_random_data,'red','Original Data')
    test4 = plot_func(anomaly_data,'blue','Anomalous Data') 
    
    test5 = plot_func(sample_data,'red','Original Data')
    test6 = plot_func(anomaly2_data,'blue','Anomalous Data') 
    
    test7 = plot_func(sample_random_data,'red','Original Data')
    test8 = plot_func(anomaly3_data,'blue','Anomalous Data') 
    
    test9 = plot_func(sample_data,'red','Original Data')
    test_10 = plot_func(anomaly4_data,'blue','Anomalous Data') 
    
    test_11 = plot_func(sample_random_data,'red','Original Data')
    test_12 = plot_func(anomaly5_data,'blue','Anomalous Data') 
