#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.

import csv, os

os.makedirs('/mnt/mymedia/workspace/Thesis/TK/Carlos/Pen_data/pen_back/ONS-Ostring1/headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir('/mnt/mymedia/workspace/Thesis/TK/Carlos/Pen_data/pen_back/ONS-Ostring1'):
    if not csvFilename.endswith('.csv'):
        print("Not a csv" + csvFilename)
        continue # skip non-csv files

    print('Reading only header from ' + csvFilename + '...')

    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open('/mnt/mymedia/workspace/Thesis/TK/Carlos/Pen_data/pen_back/ONS-Ostring1/'+csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            csvRows.append(row) # reads only first row        
    csvFileObj.close()

    # Write out the CSV file.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
