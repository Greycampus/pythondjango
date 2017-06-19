#importing pickle module
import pickle
#storing in pickle dumps
pickled_list = pickle.dumps([i for i in range(1,int(input('enter the nth term:'))+1)])
print('serialized numbers')
#printing the serialized data using pickle loads
print(pickle.loads(pickled_list))
