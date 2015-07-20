import morton
import random
import pickle

dicStorage = {}
correctResults = []

# def sanitizeInputs(x,y):
#     xmin = -90
#     xmax = 90
#     ymin = -180
#     ymax = 180
#     xi = (((x-xmin)/(xmax-xmin)) * xmax)
#     yi = (((y-ymin)/(ymax-ymin)) * ymax)
#     return (xi,yi)
def test(n):
    for i in range(n):
        x = random.uniform(-90,90)
        y = random.uniform(-180,180)
        key = morton.get_latlong_morton(x,y)
        dicStorage[key] = i
        if (x > 0 or x < 50) and (y > 0 or y < 50):
            correctResults.append(i)

    minRangeCoords = morton.get_latlong_morton(*(0,0))
    maxRangeCoords = morton.get_latlong_morton(*(50,50))
    myResults = []

    for key in dicStorage.keys():
        if (key > minRangeCoords and key < maxRangeCoords):
            myResults.append(dicStorage[key])

    return len(set(correctResults)-set(myResults)) + len(set(myResults)-set(correctResults))

def xfrange(start, stop, step):
    while start < stop:
        yield start
        start += step

power = 1
results = []
testnums = list((int(10**exp) for exp in xfrange(0,9,0.01)))
for n in testnums:
    results.append((n,test(n)))
    outfile = open('results','w')
    pickle.dump(results, outfile)
    outfile.close()
    print n





