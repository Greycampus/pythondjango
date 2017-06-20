import getpass
#getpass is used to get input hidden
sec = getpass.getpass(prompt='enter secret number for game:',stream=None)
print('player have three guesses for a 4digit number.(number range 1-6)')
for i in range(0,3):#three guesses
    k = str(raw_input('%d guess:'%(i+1)))
    scr = str()
    if(k==sec):#if guess = actual
        print('++++ you won')
        break
    else:
        for j in range(0,len(sec)):
            if(sec.find(k[j])==k.find(k[j])):
                #if position of a digit in guess = position of digit in actual number
                scr = scr+'+'
            elif(sec.count(k[j])==k.count(k[j]) and sec.find(sec[j]) != sec.find(k[j]) ):
                #if position of digit is not same but if digit exists in numbers
                scr = scr+'-'
            else:
                #if no match in position or occurence
                scr = scr+' '
        print(scr+' have another try')
print('well played')
