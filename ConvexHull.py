#  File: ConvexHull.py

#  Description:

#  Student's Name: Trey Everson

#  Student's UT EID: RHE 323

#  Partner's Name: Chase Kirkland

#  Partner's UT EID: CFK 348

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/24/19

#  Date Last Modified: 9/27/19

# This assignment was done in pair-programming

import math

class Point (object):
    # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__ (self, other):
        tol = 1.0e-8
        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol)

    def __ne__ (self, other):
        tol = 1.0e-8
        return (abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol)

    def __lt__ (self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return False
            else:
                return self.y < other.y
        return self.x < other.x

    def __le__ (self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return True
            else:
                return self.y <= other.y
        return self.x <= other.x

    def __gt__ (self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return False
            else:
                return self.y > other.y
        return self.x > other.x

    def __ge__ (self, other):
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


# computes and returns the convex hull of a sorted list of Points
# convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order
def convex_hull (sorted_points):

# compute and return the area of a convex polygon
# convex_poly is a list of Point objects that define the vertices
# of a convex polygon in order
def area_poly (convex_poly):

def main():
    # create an empty list of Point objects
    points = []
    # open file points.txt for reading
    file = open('points.txt', 'r')
# read file line by line, create Point objects and store in a list
    line = file.readline()
    num_points = line.strip()
    for points in file:
        file.readline()
        file.s

# sort the list according to x-coordinates

# get the convex hull

# print the convex hull

# get the area of the convex hull

# print the area of the convex hull

# YOU MUST WRITE THIS LINE AS IS
if __name__ == "__main__":
    main()