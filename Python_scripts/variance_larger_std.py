import numpy as np
import pandas as pd
df = pd.read_csv('/home/arun/PycharmProjects/Features/Ostring_Abgang1_01012016.csv',sep=';',decimal=",") # read_csv with decimal as '.'
a = list(df.columns.values) #returns the column names
print(a)
def variance_larger_than_standard_deviation(x):
    return np.var(x) > np.std(x)
print("Variance of W-bezug")
print(np.var(df[a[23]]))
print("Std of W-bezug")
print(np.std(df[a[23]]))
