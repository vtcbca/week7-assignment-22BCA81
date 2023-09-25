from pandas import  *

df = read_csv('Student_Data.csv')

print(df.iloc[:, 1::2])
