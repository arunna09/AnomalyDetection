#!/home/arun/anaconda2/bin/python
import MySQLdb as db1
import pandas as pd
import datetime
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

query = ("SELECT * FROM energy_sample_data1 WHERE location LIKE %(this_name)s") 
result = pd.read_sql(query,conn, params={'this_name':'Torschlag'+'%'},chunksize = 2610783)
for chunk in result:
    list_of_dfs = list.append[chunk]

print("Query executed")

df = pd.concat[list_of_dfs]

stats = df.describe()
stats.to_csv(r'/home/arun/stats_Torschlag.csv',header=True, index=True, mode='a', sep = ',')

print("Execution Completed")

now1 = datetime.datetime.now()
print "End date and time using str method of datetime object:"
print str(now1)
conn.close()
