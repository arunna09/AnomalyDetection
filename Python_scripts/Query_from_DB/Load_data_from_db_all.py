#!/home/arun/anaconda2/bin/python
import MySQLdb as db1
import pandas as pd
import datetime
import pandas.io.sql as psql
conn = db1.connect(host='127.0.0.1',
          port= 3306,
          user= 'root',
          passwd='kUrsVbpyfFWF',
          db='Energy_AD')

#cur = conn.cursor()

# Use all the SQL you like
#cur.execute("SELECT Date FROM energy_sample_data1 limit 5")

# print all the first cell of all the rows
#for row in cur.fetchall():
#    print row[0]

#conn.close()
now = datetime.datetime.now()
print "Start date and time using str method of datetime object:"
print str(now)

chunk_size = 10000
offset = 0
dfs = []
while True:
      query = ("SELECT * FROM energy_sample_data1 ORDER BY Serial_no LIMIT %d OFFSET %d" % (chunk_size,offset))
      dfs.append(psql.read_sql(query,conn))
      offset += chunk_size
      if len(dfs[-1]) < chunk_size:
         break 
dfs = pd.concat(dfs)

print("Query executed")

#Calculate the basic statistics
stats = dfs.describe()
stats.to_csv(r'/home/arun/stats_all.csv',header=True, index=True, mode='a', sep = ',')

print("Execution Completed")

now1 = datetime.datetime.now()
print "End date and time using str method of datetime object:"
print str(now1)

#Close the connection
conn.close()
