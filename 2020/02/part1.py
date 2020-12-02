def find (lower, upper, letter, password):
    count = password.count(letter)
    return (count >= lower and count <= upper)

sum = 0
filepath = 'E:/filez/projects/adventofcode/2020/02/input01.txt'
with open(filepath, "r") as file:
    for line in file:
        array = line.strip().split(' ')
        if (find(int(array[0].split('-')[0]), int(array[0].split('-')[1]), array[1].split(':')[0], array[2])):
                 sum += 1
print("Correct passwords: " + str(sum))
