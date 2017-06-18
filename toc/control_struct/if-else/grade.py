k = input('enter percentage of person:')
if(k>85):
    print('Person received grade \'A\'')
elif(k<=85 and k>80):
    print('Person received grade \'A-\'')
elif(k>70 and k<=80):
    print('Person received grade \'B\'')
elif(k>60 and k<=70):
    print('Person received grade \'C\'')
elif(k>40 and k<=60):
    print('Person received grade \'D\'')
elif(k<=40):
    print('Person received grade \'E\'')
    if(k<=35):
        print('person failed')
