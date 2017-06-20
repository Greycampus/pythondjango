#taking data in list by using split function
k = list(raw_input('enter list of your choice with repetitions:').split(' '))
print('unique items in list are')
#set is a datatype in python only stores unique items in list
#conversion list->set->list
k = list(set(k))
#printing the unique item list
print(k)
