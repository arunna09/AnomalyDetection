#comparing the headers of csv files for same columns. This file will extract only the headers of the csvs and prints all the csvs with missing I-N columns

import csv, os

#os.makedirs('/home/arun/PycharmProjects/HeaderCSV/headerRemoved', exist_ok=True)
csvRows = []
csvnRows = []
FailedCsvs = []
x = 0
# Loop through every file in the current working directory.
for csvFilename in os.listdir('/home/arun/PycharmProjects/HeaderCSV/headerRemoved'):
    if not csvFilename.endswith('.csv'):
        print("Not a csv" + csvFilename)
        continue # skip non-csv files
    csvFileObj = open('/home/arun/PycharmProjects/HeaderCSV/headerRemoved/'+csvFilename)
    readerObj = csv.reader(csvFileObj)
    
    print('Reading file ' + csvFilename + '...')
    for row in readerObj:
        #print('2')
        del csvnRows[:] #Refresh the second list to contain the new row
        if readerObj.line_num == 1:
            if x == 0 :
                csvRows.append(row) # append the row to the first list
                x = 1
                #print('1')
                continue
            else :
                csvnRows.append(row)
        if (csvRows == csvnRows):
            print('success')
        else:
            FailedCsvs.append(csvFilename) #append all the filenames which differ from Ostring_Abgang5_12012016.csv
            print('Fail ' + csvFilename)
        
    csvFileObj.close()
print(FailedCsvs) # these files have I-N column extra

