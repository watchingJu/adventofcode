import numpy as np
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"
    def __str__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return "Line(" + str(self.a) + ", " + str(self.b) + ")"
    def __str__(self):
        return "Line(" + str(self.a) + ", " + str(self.b) + ")"

    def is_between(self, c):
        return ((b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1]) and 
                abs(cmp(a[0], c[0]) + cmp(b[0], c[0])) <= 1 and
                abs(cmp(a[1], c[1]) + cmp(b[1], c[1])) <= 1)

    def cmp(a, b):
        return (a>b)-(a<b)

    def length(self):
        return abs(self.a.x - self.b.x) + abs(self.a.y - self.b.y)

x = [0]
y = [0]
counter = 0
distances = []
# one wire represented by points
wire = []
# list of multiple wires
wires = []
# list of lines
wireLines = []
# distances with length as value
distancesDictA = {}
distancesDictB = {}

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
    # for each line in the input-file
    for inputline in file:
        line = inputline.strip().split(",")
        wire.append(Point(0, 0))
        # fill first line of inputfile
        if len(x) < 2 and len(wire) < 2:
            for j in line:
                #add points to point-list
                if j[:1] == "R":
                    wire.append(
                        Point(wire[-1].x + int(j[1:]),
                              wire[-1].y + 0))
                    x.append(x[-1] + int(j[1:]))
                    y.append(y[-1] + 0)
                elif j[:1] == "L":
                    wire.append(
                        Point(wire[-1].x - int(j[1:]),
                              wire[-1].y + 0))
                    x.append(x[-1] - int(j[1:]))
                    y.append(y[-1] + 0)
                elif j[:1] == "D":
                    wire.append(
                        Point(wire[-1].x + 0,
                              wire[-1].y - int(j[1:])))
                    x.append(x[-1] + 0)
                    y.append(y[-1] - int(j[1:]))
                elif j[:1] == "U":
                    wire.append(
                        Point(wire[-1].x + 0,
                              wire[-1].y + int(j[1:])))
                    x.append(x[-1] + 0)
                    y.append(y[-1] + int(j[1:]))
                # add lines to line-list
                wireLines.append(Line(Point(wire[-2].x, wire[-2].y),
                                        Point(wire[-1].x, wire[-1].y)))
        # all following lines of the input file
        else:
            # initial points / central port
            pointA = (0, 0)
            A = Point(0, 0)
            pointB = (0, 0)
            B = Point(0, 0)
            lengthWireA = 0
            for j in line:
                pointA = (pointB[0], pointB[1])
                A = Point(B.y, B.y)
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

                lineA = Line(Point(pointA[0], pointA[1]), Point(pointB[0],pointB[1]))
                lengthWireA += lineA.length()
                lengthWireB = 0
                for indx in range(len(x) - 1):
                    C = (x[indx], y[indx])
                    D = (x[indx+1], y[indx+1])
                    
                    lineB = Line(Point(C[0], C[1]), Point(D[0],D[1]))
                    # cummulative length of lines
                    lengthWireB += lineB.length()
                    try:
                        intersection = line_intersection((pointA, pointB), (C, D))
                        if is_between(pointA, pointB, intersection) and is_between(C, D, intersection):
                            #print("\tline_intersection: ", end="")
                            #print(intersection)
                            md = manhattan_distance((0,0), intersection)
                            #print("\tmd: " + str(md))
                            distances.append(md)
                            # saves manhattan distance + wireLength minus length until intersection
                            tmpA = Line(Point(intersection[0], intersection[1]),
                                        Point(pointB[0], pointB[1]))
                            tmpB = Line(Point(intersection[0], intersection[1]),
                                        Point(D[0],D[1]))
                            distancesDictA[md] = (lengthWireA - tmpA.length())
                            distancesDictB[md] = (lengthWireB - tmpB.length())
                    except Exception as err:
                        #print("\tskipped: ", end="")
                        #print(err)
                        pass
                #print("")
                
        counter += 1
print("\n\ndistances:", end="")
print(distances)
print("min distance to intersection: ", end="")
print(min(distances))

wireLength = []
for key in distancesDictA:
    wireLength.append(distancesDictA[key] + distancesDictB[key])
print(min(wireLength))
