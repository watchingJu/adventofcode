def count_orbits(planet, listOfTuples):
    retVal = 1
    for item, x in listOfTuples:
        if item == planet:
            retVal += count_orbits(x, listOfTuples)

    return retVal

inputfile = "p1_input.txt"

values = open(inputfile, "r").read().splitlines()
listOfTuples = []
counter = 0
# make reverse tuples - not A)B -> (A, B) but (B, A)
for value in values:
    listOfTuples.append((value[4:],value[:3]))

# sort them, no idea why, maybe a dict is faster?
listOfTuples =  sorted(listOfTuples, key=lambda x: x[0])

print(listOfTuples)
print("\n")

for tup in listOfTuples:
    #print(tup[0])
    counter += count_orbits(tup[0], listOfTuples) - 1

print(counter)
