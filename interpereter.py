import pickle

results = pickle.load(open('results','r'))
for point in results:
    n,k = point
    if k != 0:
        print float(k)/float(n)