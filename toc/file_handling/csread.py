import csv
import sys
c_data = []
for d in csv.DictReader(open('cc.csv')):
    c_data.append(str(d['second']))
print('the data in second column is :')
print(c_data)
