import pickle
with open("副总裁.pkl",'rb') as f:
    list = pickle.load(f)
print(len(list))
for i in list:
    print(i)