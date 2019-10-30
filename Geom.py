#  File: Geom.py

#  Description: Working with objects using points, circles, and rectangles.

#  Student's Name: Trey Everson

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/16/19

#  Date Last Modified: 9/17/19

import math


class Point(object):
    # constructor
    # x and y are floats
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance
    # other is a Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    # takes no arguments
    # returns a string
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-8
        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol)


class Circle(object):
    # constructor
    # x, y, and radius are floats
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        self.center = Point(x, y)

    # compute cirumference
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area(self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside(self, p):
        return self.center.dist(p) < self.radius

    # determine if a circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c overlaps this circle (non-zero area of overlap)
    # but neither is completely inside the other
    # the only argument c is a Circle object
    # returns a boolean
    def circle_overlap(self, c):
        distance = self.center.dist(c.center)
        return distance <= self.radius + c.radius
    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object

    def circle_circumscribe(self, r):
        x = (r.ul.x + r.lr.x) / 2
        y = (r.ul.y + r.lr.y) / 2
        center = Point(x, y)
        radius = center.dist(r.ul)
        return Circle(radius, x, y)
    # string representation of a circle
    # takes no arguments and returns a string

    def __str__(self):
        return "Radius: " + str(self.radius) + ", Center: " + str(self.center)

    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__(self, other):
        tol = 1.0e-8
        return (abs(self.radius - other.radius)) < tol


class Rectangle(object):
    # constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if (ul_x < lr_x) and (ul_y > lr_y):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length(self):
        return self.lr.x - self.ul.x
    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float

    def width(self):
        return self.ul.y - self.ul.y
    # determine the perimeter
    # takes no arguments, returns a float

    def perimeter(self):
        return (2 * self.length()) + (2 * self.width())
    # determine the area
    # takes no arguments, returns a float

    def area(self):
        return self.length() * self.width()
    # determine if a point is strictly inside the Rectangle
    # takes a point object p as an argument, returns a boolean

    def point_inside(self, p):
        return (self.ul.x < p.x < self.lr.x) and (self.ul.y > p.y > self.lr.y)
    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal

    def rectangle_inside(self, r):
        return (self.ul.x > r.ul.x and self.ul.y > r.ul.y) and (self.lr.x > r.lr.x and self.lr.y > r.lr.y)
    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean

    def rectangle_overlap(self, r):
        return not((r.ul.x > self.lr.x) or (r.lr.x < self.ul.x) or (r.lr.y > self.ul.y) or (r.ul.y < self.lr.y))
    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object

    def rectangle_circumscribe(self, c):
        ul_x = c.center.x - c.radius
        ul_y = c.center.y + c.radius
        lr_x = c.center.x + c.radius
        lr_y = c.center.y - c.radius
        return Rectangle(ul_x, ul_y, lr_x, lr_y)
    # give string representation of a rectangle
    # takes no arguments, returns a string

    def __str__(self):
        return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

    # determine if two rectangles have the same length and width
    # takes a rectangle other as argument and returns a boolean
    def __eq__(self, other):
        tol = 1.0e-8
        return abs(self.width() - other.width() and (self.length() - other.length())) < tol


def main():
# open the file geom.txt
    file = open('geom.txt', 'r')
    coordinates = []
    for line in file:
        line = line.strip()
        words = line.split()
        for numbers in words:
            try:
                coordinates.append(float(numbers))
            except:
                continue
# create Point objects P and Q
    p = Point(coordinates[0], coordinates[1])
    q = Point(coordinates[2], coordinates[3])
# print the coordinates of the points P and Q
    print("Coordinates of P: ", p)
    print("Coordinates of P: ", q)
# find the distance between the points P and Q
    print("Distance between P and Q: ", round(p.dist(q), 2))
# create two Circle objects C and D
    c = Circle(coordinates[4], coordinates[5], coordinates[6])
    d = Circle(coordinates[7], coordinates[8], coordinates[9])
# print C and D
    print("Circle C: ", c)
    print("Circle D: ", d)
# compute the circumference of C
    print("Circumference of C: ", c.circumference())
# compute the area of D
    print("Area of D: ", d.area())
# determine if P is strictly inside C
    if c.point_inside(p):
        print("P is inside C")
    else:
        print("P is not inside C")
# determine if C is strictly inside D
    if d.circle_inside(c):
        print("C is inside D")
    else:
        print("C is not inside D")
# determine if C and D intersect (non zero area of intersection)
    if d.circle_overlap(c):
        print("C and D overlap")
    else:
        print("C and D do not overlap")
# determine if C and D are equal (have the same radius)
#     print(c.radius == d.radius)
    if c == d:
        print("C is equal to D")
    else:
        print("C is not equal to D")
# create two rectangle objects G and H
    g = Rectangle(coordinates[10], coordinates[11], coordinates[12], coordinates[13])
    h = Rectangle(coordinates[14], coordinates[15], coordinates[16], coordinates[17])
# print the two rectangles G and H
    print("Rectangle G: ", g)
    print("Rectangle H: ", h)
# determine the length of G (distance along x axis)
    print("Length of G: ", g.length())
# determine the width of H (distance along y axis)
    print("Width of H: ", h.width())
# determine the perimeter of G
    print("Perimeter of G: ", g.perimeter())
# determine the area of H
    print("Area of H: ", h.area())
# determine if point P is strictly inside rectangle G
    if g.point_inside(p):
        print("P is inside G")
    else:
        print("P is not inside G")
# determine if rectangle G is strictly inside rectangle H
    if h.rectangle_inside(g):
        print("G is inside H")
    else:
        print("G is not inside H")
# determine if rectangles G and H overlap (non-zero area of overlap)
    if g.rectangle_overlap(h):
        print("G does overlap H")
    else:
        print("G does not overlap H")
# find the smallest circle that circumscribes rectangle G
# goes through the four vertices of the rectangle
    print("Circle that circumscribes G: ", Circle().circle_circumscribe(g))
# find the smallest rectangle that circumscribes circle D
# all four sides of the rectangle are tangents to the circle
    print("Rectangle that circumscribes D: ", Rectangle().rectangle_circumscribe(d))
# determine if the two rectangles have the same length and width
#     print((g.width() == h.width()) and (g.length() == h.length()))
    if g == h:
        print("Rectangle G is equal to H")
    else:
        print("Rectangle G is not equal to H")
# close the file geom.txt
    file.close()
# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN


if __name__ == "__main__":
    main()
