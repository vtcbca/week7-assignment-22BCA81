from csv import *

header = ['Prod_No','Prod_Name','Jan','Feb','Mar','Apr','May','Jun']
with open('Student_Data.csv','w',newline="") as File_Write:
    file_data = writer(File_Write)
    file_data.writerow(header)
