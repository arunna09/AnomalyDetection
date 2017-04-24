#inject anomalies at any position in the data, along with a parameter to introduce the number of anomaly point from injected position
#input:
	#num: Original data array.
	#mid_pos: selected point to insert anomaly, it can be any value provided the below condition is satisfied.
	#x: percentage increase of selected point i.e the anomaly point to be added.
	#count: number of points to be injected/updated to make it anomaly from the mid point.
#output:
	#t_num: returns the injected array
def add_anomaly_dynamically(num,x,count,mid_pos):
    t_num = list(num)
    if (mid_pos + count >= len(t_num)) and (mid_pos - count < 0):
        print "Point of injection is not suitable for injecting anomalies"
    else:
        #t_num.sort() #changed to work on multidimensional data, uncomment if its a 1D-array data
        last_idx = len(t_num)
        delta = 1.0 + (float(x)/float(100))
        new_list_test = [t_num[mid_pos]]
        for j in range(0,count):
            a = mid_pos - j
            b = mid_pos + j
            new_list_test.append(t_num[a])
            new_list_test.append(t_num[b])
            new_list_test.sort()
        mu = len(new_list_test)/2 
        increment = new_list_test[mu] * delta
        
        for k in range(mid_pos-count,mid_pos+count+1):
            if k == mid_pos:
                t_num[k] = increment
            else:
                increment_new = increment - new_list_test[mu]
                share = abs(mid_pos - k )
                t_num[k] = t_num[k] + increment_new * (1.0 - (float(share)/float(mu)))
    return t_num   
