from pandas import *

Column=['Product No', 'Product Name', 'January', 'February', 'March', 'April', 'May', 'June']
dtf = read_csv('Student_Data.csv')

print(dtf.tail())
