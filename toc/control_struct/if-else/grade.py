#finding grades
k = input('enter percentage of person:')
if(k>85):#if percent > 85 --A
    print('Person received grade \'A\'')
elif(k<=85 and k>80):#80<percent80=85  --A-
    print('Person received grade \'A-\'')
elif(k>70 and k<=80):#70<percent<=80 --B
    print('Person received grade \'B\'')
elif(k>60 and k<=70):#60<percent<=70  --C
    print('Person received grade \'C\'')
elif(k>40 and k<=60):#40<percent<=60  --D
    print('Person received grade \'D\'')
elif(k<=40):#percent<=40  --E 
    print('Person received grade \'E\'')
    if(k<=35):#failed condition
        print('person failed')
