import pickle

d = pickle.load(open("synonyms.pck"))

for i,y in d.items():
    print(i +" synonyms",y)
