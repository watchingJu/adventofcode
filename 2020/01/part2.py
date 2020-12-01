import itertools


def find (array):
    for i in range(len(array)):
        for j in itertools.combinations(array, i):
            if sum(map(int,j)) == target and len(j) == 3:
                print(j)
                return j


target = 2020
with open(r"E:/filez/projects/adventofcode/2020/01/input01.txt") as file:
    array = file.readlines()
goal = find(array)
print(int(goal[0]) * int(goal[1]) * int(goal[2]))
