#  File: Intervals.py

# Description: The aim in this assignment is take a set of intervals and collapse all the overlapping intervals and
# print the smallest set of non-intersecting intervals in ascending order of the lower end of the interval.

#  Student's Name: Trey Everson

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/7/19

#  Date Last Modified: 9/9/19


import numpy as np


def merge_tuple(sorted_list):
    sorted_list = sorted(sorted_list, key=lambda tup: tup[0])
    s = []

    for i in sorted_list:  # Merge sort loop
        if not s:
            s.append(i)
        else:
            b = s.pop()
            if b[1] >= i[0]:
                new_tuple = (b[0], max(b[1], i[1]))  # Add the larger value into the new tuple
                s.append(new_tuple)
            else:
                s.append(b)
                s.append(i)
    return s


def sort_non_intersect(sorted_list):
    i = sorted(set([tuple(sorted(i)) for i in sorted_list]))

    f = [i[0]]
    for c, d in i[1:]:
        a, b = f[-1]
        if c <= b < d:
            f[-1] = a, d
        elif b < c < d:
            f.append((c, d))
        else:
            pass
    return f


num = open('intervals.txt', 'r')
num = num.read().split()
new_tuple = []
for i in range(0, len(num), 2):
    intervals = (int(num[i]), int(num[i+1]))
    new_tuple.append(intervals)

answer = list(sort_non_intersect(new_tuple))
print("Non-intersecting Intervals: ")
for i in range(len(answer)):
    print(answer[i])

print("")

merged = merge_tuple(new_tuple)
merged = sorted(merged, key=lambda tup: tup[1]-tup[0])
print("Non-intersecting Intervals in order of size: ")
for intervals in merged:
    print(intervals)

