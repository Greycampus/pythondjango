n  = int(raw_input())
names = []
marks = []
for i in range(0,n):
    names.append(str(raw_input()))
    marks.append(float(raw_input()))
dd = zip(names,marks)
dd = sorted(dd,key= lambda x: (x[1], x[0]))
marks = sorted(marks)
sm = sorted(list(set(marks)))
sms = marks.count(sm[1])
sml = marks.count(sm[0])
oo = [x[0] for x in dd]
for i in range(sml,sms+sml):
    print(oo[i])
