# solution - 370
import time

tmp=""

def count_orbits(planet, listOfTuples):
    global tmp
    orbits = 1
    for item, x in listOfTuples:
        if item == planet:
            tmp += x
            orbits += count_orbits(x, listOfTuples)
    return orbits

def move(ways, n):
    for i in range(0, len(ways[0]), n):
        if ways[1].find(ways[0][i:i+n]) >= 0 and ways[1].find(ways[0][i:i+n]) % n == 0:
            #print(ways[0][i:i+n])
            a = ways[1].find(ways[0][i:i+n])
            #print(a)
            #print(i)
            return int((a/n + i/n) - 2)
    return 0

def calculation(inputfile, wFrom, wTo, n):
    global tmp
    values = open(inputfile, "r").read().splitlines()

    listOfTuples = []
    for value in values:
        listOfTuples.append((value[n+1:],value[:n]))
    listOfTuples =  sorted(listOfTuples, key=lambda x: x[0])
    
    #print(listOfTuples)
    #print("\n")
    
    counter = 0
    ways = []
    for tup in listOfTuples:
        tmp=""
        if tup[0] == wFrom or tup[0]== wTo:
            tmp += tup[0]
        #print(tup[0])
        counter += count_orbits(tup[0], listOfTuples) - 1
        if tup[0] == wFrom or tup[0]== wTo:
            ways.append(tmp)

    print("\"" + inputfile + "\" has ", end="")
    print(counter, end="")
    print(" orbits in total")
    #print("ways: ",end="")
    #print(ways)
    print(wFrom + " moved ", end="")
    print(move(ways, n), end="")
    print(" orbits to " + wTo)

# test data
inputfile = "p2_test0.txt"
wFrom = "X"
wTo = "Y"
n=1

t = time.time()
calculation(inputfile, wFrom, wTo, n)
print("calculated in ",end="")
print(time.time() - t)

print("\n#################################\n")

# input data
inputfile = "p2_input.txt"
wFrom = "YOU"
wTo = "SAN"
n=3 #len of IDs

t = time.time()
calculation(inputfile, wFrom, wTo, n)
print("calculated in ",end="")
print(time.time() - t)
