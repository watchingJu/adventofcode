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
    print("\tdebugoutput: " + str(lines[int(index+1)]))
    if int((int(lines[index]) / 100) % 10) == 1:
        param1 = lines[index+1]
    else:
        param1 = lines[int(lines[index+1])]
    return param1

################################

# jump-if-true
def jumpIfTrue(lines, index):
    print("jumpIfTrue: ", end="")
    if int((int(lines[index]) / 100) % 10) == 1:
        param1 = lines[index+1]
    else:
        param1 = lines[int(lines[index+1])]
    print(param1, end="")
    if int((int(lines[index]) / 1000) % 10) == 1:
        param2 = lines[index+2]
    else:
        param2 = lines[int(lines[index+2])]
    print(", ", end="")
    print(param2)

    if int(param1) != 0:
        return param2
    else:
        return index + 3


# jump-if-false
def jumpIfFalse(lines, index):
    print("jumpIfFalse: ", end="")
    if int((int(lines[index]) / 100) % 10) == 1:
        param1 = lines[index+1]
    else:
        param1 = lines[int(lines[index+1])]
    print(param1, end="")
    if int((int(lines[index]) / 1000) % 10) == 1:
        param2 = lines[index+2]
    else:
        param2 = lines[int(lines[index+2])]
    print(", ", end="")
    print(param2)

    if int(param1) == 0:
        return param2
    else:
        return index + 3


# less than
def lessThan(lines, index):
    print("lessThan: ",end="")
    if int((int(lines[index]) / 100) % 10) == 1:
        param1 = lines[index+1]
    else:
        param1 = lines[int(lines[index+1])]
    print(param1,end="")
    if int((int(lines[index]) / 1000) % 10) == 1:
        param2 = lines[index+2]
    else:
        param2 = lines[int(lines[index+2])]
    print(", ",end="")
    print(param2,end="")

    # write is never immediate
    param3 = lines[index+3]
    print(", ",end="")
    print(param3)

    if int(param1) < int(param2):
        lines[int(param3)] = "1"
    else:
        lines[int(param3)] = "0"
    
    return lines



# equals
def equals(lines, index):
    print("equals: ", end="")
    if int((int(lines[index]) / 100) % 10) == 1:
        param1 = lines[index+1]
    else:
        param1 = lines[int(lines[index+1])]
    print(param1, end="")
    if int((int(lines[index]) / 1000) % 10) == 1:
        param2 = lines[index+2]
    else:
        param2 = lines[int(lines[index+2])]
    print(", ", end="")
    print(param2,end="")
    
    # write is never immediate
    param3 = lines[index+3]
    print(", ",end="")
    print(param3)
    
    
    if int(param1) == int(param2):
        lines[int(param3)] = "1"
    else:
        lines[int(param3)] = "0"
    
    return lines


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
#####################################
        elif opcode == 5:
            index = int(jumpIfTrue(lines, index))
        elif opcode == 6:
            index = int(jumpIfFalse(lines, index))
        elif opcode == 7:
            lines = lessThan(lines, index)
            index += 4
        elif opcode == 8:
            lines = equals(lines, index)
            index += 4
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
#inputfile = "p2_test03.txt"

lines = open(inputfile, "r").read().split(',')

userinput = input("input: ")

print(lines)
print()
print("diagnostic code: " + main(lines).lstrip("0"))
#print(lines)