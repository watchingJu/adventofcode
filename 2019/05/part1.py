import re
#global lines
index = 0

# add
def add(lines, index):
    print("add")
    if int((int(lines[index]) / 100) % 10) == 1:
        param1 = lines[index+1]
    else:
        param1 = lines[int(lines[index+1])]

    if int((int(lines[index]) / 1000) % 10) == 1:
        param2 = lines[index+2]
    else:
        param2 = lines[int(lines[index+2])]
    lines[int(lines[index+3])] = int(param1) + int(param2)
    #print(lines)
    return lines

# multiply
def multiply(lines, index):
    print("multiply")
    if int((int(lines[index]) / 100) % 10) == 1:
        param1 = lines[index+1]
    else:
        param1 = lines[int(lines[index+1])]

    if int((int(lines[index]) / 1000) % 10) == 1:
        param2 = lines[index+2]
    else:
        param2 = lines[int(lines[index+2])]

    lines[int(lines[index+3])] = int(param1) * int(param2)
    #print(lines)
    return lines

# input
def setInput(lines, index):
    global userinput
    print("setInput")
    lines[int(lines[index+1])] = userinput
    return lines

# output
def getOutput(lines, index):
    print("getOutput")
    #print("\tdebugoutput: " + str(lines[int(lines[index+1])]))
    if int((int(lines[index]) / 100) % 10) == 1:
        return lines[index+1]
    else:
        return lines[int(lines[index+1])]


def main(lines):
    index = 0
    output = ""
    # last element used?
    while index < len(lines):
        print("index: " + str(index))
        cmd = lines[index]
        print("value[" + str(index) + "]: " + str(cmd))

        opcode = int(int(cmd) % 10)
        print("opcode: ",end="")
        print(opcode)

        if opcode == 1:
            lines = add(lines, index)
            index += 4
        elif opcode == 2:
            lines = multiply(lines, index)
            index += 4
        elif opcode == 3:
            lines = setInput(lines, index)
            index += 2
        elif opcode == 4:
            output = output + str(getOutput(lines, index))
            index += 2
        elif opcode == 0:
            print("error")
            return ""
        elif opcode == 9:
            if int(int(cmd) % 100) == 99:
                break
        print("")

    # print("index: " + str(index))
    return output


inputfile = "input.txt"
#inputfile = "test01.txt"

f = open(inputfile, "r")
lines = f.read().split(',')
f.close()

userinput = input("input: ")

print(lines)
print()
print("diagnostic code: " + main(lines).lstrip("0"))