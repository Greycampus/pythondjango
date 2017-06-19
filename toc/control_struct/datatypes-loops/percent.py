n = int(raw_input())
marks = []
for _ in range(n):
    marks.append(list(raw_input().split(' ')))
q = str(raw_input())
naa = [x[0] for x in marks]
e = naa.index(q)
#print(marks[e])
tm = marks[e]
re = float(tm[1])+float(tm[2])+float(tm[3])
re = re/3
print("%.2f" % re)
