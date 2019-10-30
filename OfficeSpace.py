#  File: OfficeSpace.py

#  Description: Working with objects.

#  Student's Name: Trey Everson

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/20/19

#  Date Last Modified: 9/23/19


class Office(object):
    def __init__(self, l = 0, w = 0, n = 0, data = []):
        self.l = l
        self.w = w
        self.n = n
        self.data = []

    def add_employee(self, employee = []):
        self.data.append(employee)

    def area(self):
        return self.l * self.w

    def overlap(self, employee1, employee2):
        if employee1[1] > employee2[3] or employee1[3] < employee2[1]:
            return False
        if employee1[2] > employee2[4] or employee1[4] < employee2[2]:
            return False
        else:
            return True

    # def intersects(self, other):
    #     return not (self.top_right.x < other.bottom_left.x or self.bottom_left.x > other.top_right.x or
    #                 self.top_right.y < other.bottom_left.y or self.bottom_left.y > other.top_right.y)

    def contested(self):
        for i in range(0, len(self.data) - 1):
            return abs(self.data[i][1] - self.data[i + 1][1]) * abs(self.data[i][4] - self.data[i + 1][4])


class Employee(object):
    def __init__(self, name = ' ', x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.name = ''
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def area(self):
        return abs(self.x1 - self.x2) * abs(self.y1 - self.y2)

    def employee_data(self):
        return self.name, self.x1, self.y1, self.x2, self.y2


def main():
    # open file
    file = open('office.txt', 'r')
    while True:
        line = file.readline()
        if line == '\n':    # new line at end of file
            return -1
        else:
            office = Office()   # create new office object

            dimensions = line.strip()
            dimensions = dimensions.split(' ')
            office.l = int(dimensions[0])
            office.w = int(dimensions[1])
            unallocated = Office.area(office)   # set unallocated variable equal to office area for later calculations
            # print(unallocated)
            # unallocated = unallocated + office.contested()
            print("Total " + str(Office.area(office)))

            employee_count = file.readline()
            employee_count = employee_count.strip()
            employee_count = int(employee_count)

            # create a dictionary for output formatting according to assignment
            dict = {}

            # getting each employee's data from the file
            for i in range(0, employee_count):
                employee = Employee()
                line = file.readline()
                line = line.strip()
                line = line.split(" ")
                employee.name = str(line[0])
                employee.x1 = int(line[1])
                employee.y1 = int(line[2])
                employee.x2 = int(line[3])
                employee.y2 = int(line[4])

                employee_list = employee.employee_data()
                office.add_employee(employee_list)

                dict[employee.name] = Employee.area(employee)

                unallocated = unallocated - Employee.area(employee)
                # print("Unallocated " + str(unallocated))
                # print("Contested " + str(office.contested()))

                # print(employee.name, Employee.area(employee))
            is_contested = office.contested()
            is_contested = int(is_contested)
            # print(is_contested)
            # adding back contested space because it gets subtracted twice
            unallocated = unallocated + office.contested()
            # unallocated = unallocated - Employee.area(employee)
            print("Unallocated " + str(unallocated))
            print("Contested " + str(office.contested()))
            # print(dict)
            # updating the employee's area if they have contested space
            for i in range(0, len(office.data)-2):
                for j in range(i + 1, len(office.data)-1):
                    if office.overlap(office.data[i], office.data[j]):
                        a1 = dict[office.data[i][0]] - is_contested
                        dict[office.data[i][0]] = a1
                        a2 = dict[office.data[j][0]] - is_contested
                        dict[office.data[j][0]] = a2
            # dictionary with formatted data
            for key in dict:
                print(key + " " + str(dict[key]))
            print()


main()
