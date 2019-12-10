#global lines
#global index

def one(index, lines):
    print("one")
    lines[lines[index+3]] = int(lines[lines[index+1]]) + int(lines[lines[index+2]])
    print(lines)
    return lines

def two(index, lines):
    print("two")
    lines[lines[index+3]] = int(lines[lines[index+1]]) * int(lines[lines[index+2]])
    print(lines)
    return lines

def nounverb(noun, verb, lines):
    lines[1] = noun
    lines[2] = verb
    return lines

def main(lines):
    for index in range(0, len(lines), 4):
        try:
            lines[index] = int(lines[index])
            lines[index+1] = int(lines[index+1])
            lines[index+2] = int(lines[index+2])
            lines[index+3] = int(lines[index+3])
        except:
            print()

        print("value[" + str(index) + "]: " + str(lines[index]))
        if lines[index] == 1:
            lines = one(index, lines)
        elif lines[index] == 2:
            lines = two(index, lines)
        elif lines[index] == 99:
            break
    print("index: " + str(index))
    return lines


goal = int(19690720)
inputfile = "input.txt"

for i in range(0, 99):
    for j in range(0,99):
        f = open(inputfile, "r")
        lines = f.read().split(',')
        f.close()

        lines = nounverb(i, j, lines)
        lines = main(lines)
        if lines[0] == goal: break
    if lines[0] == goal: break