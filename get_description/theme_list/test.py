import pickle
with open('theme_list.pkl',"rb") as f:
    a = pickle.load(f)
print(a)
