#  File: Bridge.py

#  Description:

#  Student's Name: Trey Everson

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 10/1/19

#  Date Last Modified: 10/6/19


def bridge_time2(data, n):
    if n < 3:
        return data[n - 1]
    elif n == 3:
        return data[0] + data[1] + data[2]
    else:
        temp1 = data[n - 1] + data[0] + data[n - 2] + data[0]
        temp1 = int(temp1)
        temp2 = data[1] + data[0] + data[n - 1] + data[1]
        temp2 = int(temp2)

        if temp1 < temp2:
            return temp1 + bridge_time2(data, n - 2)
        elif temp2 < temp1:
            return temp2 + bridge_time2(data, n - 2)
        else:
            return temp2 + bridge_time2(data, n - 2)


def main():
    # open file for reading
    in_file = open('bridge.txt', 'r')
    data = []

    line = in_file.readline()
    line = line.strip('\n')
    num_cases = int(line)
    # print (num_cases)
    line = in_file.readline()

    # iterate through file using a nested for loop
    for i in range(0, num_cases):
        line = in_file.readline()
        n = int(line)
        for j in range(n):
            line = in_file.readline()
            number = int(line)
            data.append(number)

        data.sort()
        print(bridge_time2(data, n))
        print()
        line = in_file.readline()
        data = []

        # l = [25, 5, 15, 2]
    # n = len(l)
    # n = int(n)
    # l.sort()
    # print(bridge_time2(l, n))


main()
