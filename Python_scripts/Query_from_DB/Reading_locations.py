import datetime
import numpy as np

now = datetime.datetime.now()
print "Start date and time using str method of datetime object:"
print str(now)

df = query('select distinct Location from energy_sample_data1')
df.to_csv('locations.csv', sep=',', encoding='utf-8',index=False)

now1 = datetime.datetime.now()
print "End date and time using str method of datetime object:"
print str(now1)
