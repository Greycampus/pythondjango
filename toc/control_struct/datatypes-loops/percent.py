#take in user input with multiple types in string format
n = int(raw_input())
marks = []
for _ in range(n):
    #making list of raw data
    marks.append(list(raw_input().split(' ')))
#get name for percentage finding
q = str(raw_input())
#get name using list comprehension
naa = [x[0] for x in marks]
#finding index of student using index() function
e = naa.index(q)
#extracting student data
tm = marks[e]
#summing the marks
re = float(tm[1])+float(tm[2])+float(tm[3])
#finding average to get marks
re = re/3
print("%.2f" % re)
