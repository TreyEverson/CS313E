#  File: ConvexHull.py

#  Description: Determining if a set of points is a convex hull and getting area.

#  Student's Name: Trey Everson

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/24/19

#  Date Last Modified: 9/27/19


import math


class Point (object):
    # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__(self, other):
        tol = 1.0e-8
        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol)

    def __ne__(self, other):
        tol = 1.0e-8
        return (abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol)

    def __lt__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return False
            else:
                return self.y < other.y
        return self.x < other.x

    def __le__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return True
            else:
                return self.y <= other.y
        return self.x <= other.x

    def __gt__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return False
            else:
                return self.y > other.y
        return self.x > other.x

    def __ge__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return True
            else:
                return self.y >= other.y
        return self.x >= other.x

# compute and return the determinant of the coordinates of three points
# p, q, and r are Point objects
def det (p, q, r):
    sum1 = q.x * r.y + p.x * q.y + r.x * p.y
    sum2 = q.x * p.y + r.x * q.y + p.x *r.y
    return sum1 - sum2

def is_right_turn(p, q, r):
    assert p != q and q != r and p != r
    return det(p, q, r) < 0

# computes and returns the convex hull of a sorted list of Points
# convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order
def convex_hull(sorted_points):
    n = int(len(sorted_points))
    upper = [sorted_points[0], sorted_points[1]]
    # iterate through list of sorted points to create the upper hull
    for p in sorted_points[2:]:
        upper.append(p)
        while len(upper) > 2 and not is_right_turn(upper[-3], upper[-2], upper[-1]):
            del upper[-2]

    # reverse points
    sorted_points.reverse()
    lower = [sorted_points[0], sorted_points[1]]
    for p in sorted_points[2:]:
        lower.append(p)
        while len(lower) > 2 and not is_right_turn(lower[-3], lower[-2], lower[-1]):
            del lower[-2]

    # delete duplicate points
    del lower[0]
    del lower[-1]

    # return the upper and lower hull points in a tuple for output purposes
    return tuple(upper + lower)

# compute and return the area of a convex polygon
# convex_poly is a list of Point objects that define the vertices
# of a convex polygon in order
def area_poly (convex_poly):
    area = 0
    n = len(convex_poly)
    for i in range(0, n):
        area = area + (convex_poly[i-1].x + convex_poly[i].x) * (convex_poly[i-1].y - convex_poly[i].y)
    area = 0.5 * abs(area)
    return area

def main():
    # create an empty list of Point objects
    points = []
    # open file points.txt for reading
    file = open('points.txt', 'r')
# read file line by line, create Point objects and store in a list
    line = file.readline()
    n = line.strip()
    n = int(n)
    for i in range(1, n + 1):
        line = file.readline()
        # num_points = line.strip()
        line = line.strip()
        coordinates = line.split()
        # num_points = int(num_points)
        px = int(coordinates[0])
        py = int(coordinates[1])
        p = Point(px, py)
        points.append(p)

# sort the list according to x-coordinates
    points = sorted(points)
# get the convex hull
    hull = convex_hull(points)
# print the convex hull
    print('Convex Hull')
    for i in hull:
        print(i)
    print()
# get the area of the convex hull
    area = area_poly(hull)
# print the area of the convex hull
    print("Area of Convex Hull = " + str(area))
# YOU MUST WRITE THIS LINE AS IS
if __name__ == "__main__":
    main()
