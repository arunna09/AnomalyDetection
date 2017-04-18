#!/bin/bash
now=$(date +"%T") | #loop through the folder containing .csv files and execute the load file command to load into the Energy_AD.energy_sample_data1 table.
echo "Start time : $now"
for f in *.csv
do
mysql -u root -pkUrsVbpyfFWF Energy_AD -Bse "load data local infile '$f'
                into table Energy_AD.energy_sample_data1
                FIELDS TERMINATED BY ';'
                ENCLOSED BY '\"'
                LINES TERMINATED BY '\n'
                IGNORE 1 LINES
(@c,@d,Time,@p,@Unit1,@q,@Unit2,@r,@Unit3,@s,@Unit4,@t,@Unit5,@u,@Unit6,@v,@Unit7,@w,@Unit8,@x,@Unit9,@y,@Unit10,@z,@Unit11,@a,@Unit12,Location)
set Date = STR_TO_DATE(@d,'%d.%m.%Y'),V1 = REPLACE(@p,',','.'),V2 = REPLACE(@q,',','.'),V3 = REPLACE(@r,',','.'),I1 = REPLACE(@s,',','.'),I2 = REPLACE(@t,',','.'),I3 = REPLACE(@u,',','.'),I_N = REPLACE(@v,',','.'),Pges=REPLACE(@w,',','.'),Sges=REPLACE(@x,',','.'),CosPhi = REPLACE(@y,',','.'),Egy_trpt = REPLACE(@z,',','.'),Egy_con = REPLACE(@a,',','.'), Location = '$f';COMMIT;"
endtime=$(date +"%T")
echo "End time : $endtime"
done

