import pickle
pickled_list = pickle.dumps([i for i in range(1,int(input('enter the nth term:'))+1)])
print('serialized numbers')
print(pickle.loads(pickled_list))
