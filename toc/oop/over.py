class A():

    def __init__(self):
        self.__x = 1

    #def m1(self):
    #    print("m1 from A")
    def m1(self,Ab):
        print('A\'s:'+str(Ab))


class B(A):

    def __init__(self):
        self.__y = 1

    #def m1(self):
    #    print("m1 from B")
    def m1(self,Ab):
        print('B\'s:'+str(Ab))

c = B()
#c.m1()
c.m1('hello')
