from pandas import *

dtf = read_csv('Student_Data.csv')

print(dtf[['Prod_No','Prod_Name','Jan']])
