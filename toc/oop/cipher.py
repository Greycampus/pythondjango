import re
class cipher:
    """docstring for ."""
    def __init__(self, tst,sh):
        self.tst = tst


class icipher(cipher):
    def __init__(self,tst,sh):
        cipher.__init__(self,tst,sh)
        self.sh = sh
    def bre(self):
        print('entered plain text:'+str(self.tst))
        csr =self.tst
        cc = str()
        for i in range(0,len(self.tst)):
            if(ord(csr[i])>117):
                #print('1')
                cc =cc+''.join(chr(ord(csr[i])-26+self.sh))
            else:
                #print('2')
                cc= cc+''.join(chr(ord(csr[i])+int(self.sh)))
        print('cipher text is:'+str(cc))
    def pp(self):
        print('entered plain text:'+str(self.tst))
txt = raw_input('enter the text to encrypted:')
sht = int(input('enter shift for cisear cipher:'))
k = icipher(txt,sht)
k.bre()
