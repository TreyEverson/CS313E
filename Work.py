#  File: Work.py

#  Description: Modifying binary search

#  Student Name:  Trey Everson

#  Student UT EID:  RHE 323

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/27/19

#  Date Last Modified: 9/30/19


def binary_search(n, k, low, high):
    while high > low:
        mid = (low + high) // 2
        if has_enough(mid, n, k) == 1:
            if has_enough(mid - 1, n, k) == 0:
                return mid
            else:
                high = mid
        else:
            low = mid


def has_enough(mid, n, k):
    p = 1
    finished = mid
    cont = 1

    while cont == 1:
        wrote = mid // (k ** p)
        if wrote == 0:
            if finished >= n:
                return 1
            else:
                return 0
        else:
            finished = finished + wrote
            p += 1


def main():
    file = open('work.txt', 'r')

    line = file.readline()
    T = line.strip()
    T = int(T)
    for i in range(1, T + 1):
        line = file.readline()
        line = line.strip()
        vals = line.split(" ")
        n = int(vals[0])
        k = int(vals[1])

        low = 1
        high = n

        print(binary_search(n, k, low, high))


main()
