import getpass
sec = getpass.getpass(prompt='enter secret number for game:',stream=None)
print('player have three guesses for a 4digit number.(number range 1-6)')
for i in range(0,3):
    k = str(raw_input('%d guess:'%(i+1)))
    scr = str()
    if(k==sec):
        print('++++ you won')
        break
    else:
        for j in range(0,len(sec)):
            if(sec.find(k[j])==k.find(k[j])):
                #print('1')
                scr = scr+'+'
            elif(sec.count(k[j])==k.count(k[j]) and sec.find(sec[j]) != sec.find(k[j]) ):
                #print('2')
                scr = scr+'-'
            else:
                scr = scr+' '
        print(scr+' have another try')
print('well played')
