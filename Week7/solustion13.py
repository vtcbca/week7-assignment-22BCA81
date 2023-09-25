from pandas import  *

df = read_csv('Student_Data.csv')

print(df.sort_values(by="Prod_Name"))
