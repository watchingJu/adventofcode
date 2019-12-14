class Node(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []
    def add_child(self, obj):
        self.children.append(obj)

def main(lines):
    for index in range(0, len(lines)):
        print("value[" + str(index) + "]: " + str(lines[index]))

        if lines[index] == 1:
            lines = one(index, lines)
        elif lines[index] == 2:
            lines = two(index, lines)
        elif lines[index] == 99:
            break
    print("index: " + str(index))
    return lines

def count_orbits(planet, listOfTuples):
    retVal = 1
    for item, x in listOfTuples:
        if item == planet:
            retVal += count_orbits(x, listOfTuples)

    return retVal

inputfile = "input.txt"
#inputfile = "test0.txt"

values = open(inputfile, "r").read().splitlines()
listOfTuples = []
counter = 0
for value in values:
    listOfTuples.append((value[4:],value[:3]))
    #listOfTuples.append((value[2:],value[:1]))

listOfTuples =  sorted(listOfTuples, key=lambda x: x[0])

print(listOfTuples)
print("\n")

for tup in listOfTuples:
    #print(tup[0])
    counter += count_orbits(tup[0], listOfTuples) - 1

print(counter)
