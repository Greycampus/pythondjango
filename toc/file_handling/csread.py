#import csv module
import csv
import sys
c_data = []
#using DictReader in csv for getting data column wise that is first row is used for referring the rows below
#open csv file cc.csv and see it for yourself for better understanding
#if you want to know more modules in csv type dir(csv) in python shell after import csv or simply go for python docs online
for d in csv.DictReader(open('cc.csv')):
    c_data.append(str(d['second']))
print('the data in second column is :')
print(c_data)
