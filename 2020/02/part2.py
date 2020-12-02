def find (lower, upper, letter, password):
    return (bool(password[lower-1] == letter) ^ bool(password[upper-1] == letter))

sum = 0
filepath = 'input01.txt'
with open(filepath, "r") as file:
    for line in file:
        array = line.strip().split(' ')
        if (find(int(array[0].split('-')[0]), int(array[0].split('-')[1]), array[1].split(':')[0], array[2])):
                 sum += 1
print("Correct passwords: " + str(sum))
