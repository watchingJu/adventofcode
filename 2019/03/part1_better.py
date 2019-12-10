import numpy as np
import math

x = [0]
y = [0]
counter = 0
distances = []

filename = "input.txt"

# is point on line
def is_between(a,b,c):
    return ((b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1]) and 
                abs(cmp(a[0], c[0]) + cmp(b[0], c[0])) <= 1 and
                abs(cmp(a[1], c[1]) + cmp(b[1], c[1])) <= 1)
def cmp(a, b):
    return (a>b)-(a<b)

def get_intersect(a1, a2, b1, b2):
    """ 
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([a1,a2,b1,b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return (x/z, y/z)

def line_intersection(line1, line2):
    if line1[0] == line2[0] or line1[1] == line2[1]:
        raise Exception("startingpoint or endpoint are the same")
    
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    px = det(d, xdiff) / div
    py = det(d, ydiff) / div
    return px, py

def manhattan_distance(pointA, pointB):
    return abs(pointA[0] - pointB[0]) + abs(pointA[1] - pointB[1])


with open(filename, "r") as file:
    for i in file:
        line = i.strip().split(",")
        print(line)
        # fill first line
        if len(x) < 2:
            for j in line:
                if j[:1] == "R":
                    x.append(x[-1] + int(j[1:]))
                    y.append(y[-1] + 0)
                elif j[:1] == "L":
                    x.append(x[-1] - int(j[1:]))
                    y.append(y[-1] + 0)
                elif j[:1] == "D":
                    x.append(x[-1] + 0)
                    y.append(y[-1] - int(j[1:]))
                elif j[:1] == "U":
                    x.append(x[-1] + 0)
                    y.append(y[-1] + int(j[1:]))
            #print(x)
            #print(y)
        else:
            pointA = (0, 0)
            pointB = (0, 0)
            for j in line:
                pointA = (pointB[0], pointB[1])
                if j[:1] == "R":
                    pointB = (pointA[0] + int(j[1:]),
                        pointA[1] + 0)
                elif j[:1] == "L":
                    pointB = (pointA[0] - int(j[1:]),
                        pointA[1] + 0)
                elif j[:1] == "D":
                    pointB = (pointA[0] + 0,
                        pointA[1] - int(j[1:]))
                elif j[:1] == "U":
                    pointB = (pointA[0] + 0,
                        pointA[1] + int(j[1:]))
                # lines from A to B
                #print("(A, B): ", end="")
                #print(pointA, end="")
                #print(pointB)
                for indx in range(len(x) - 1):
                    C = (x[indx], y[indx])
                    D = (x[indx+1], y[indx+1])
                    #print("\t(C, D): ", end="")
                    #print(C, end="")
                    #print(D)
                    try:
                        intersection = line_intersection((pointA, pointB), (C, D))
                        if is_between(pointA, pointB, intersection) and is_between(C, D, intersection):
                            #print("\tline_intersection: ", end="")
                            #print(intersection)
                            md = manhattan_distance((0,0), intersection)
                            #print("\tmd: " + str(md))
                            distances.append(md)
                    except Exception as err:
                        #print("\tskipped: ", end="")
                        #print(err)
                        pass
                #print("")
                
        counter += 1
print("\n\ndistances:", end="")
print(distances)
print(min(distances))
