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

f = open("input.txt", "r")
#f = open("test2.txt", "r")
lines = f.read().split(',')
f.close()
print(lines)
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

print(lines)
#no 149 too low