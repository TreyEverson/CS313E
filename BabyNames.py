#  File: BabyNames.py

#  Description: Complete a program that allows a user 
#  to query a data base of the 1000 most popular baby names 
#  in the United States per decade for the past 11 decades
#  under the constraints described below. As always, you may
#  add helper functions and should do so to provide structure
#  to the program and reduce redundancy.
#  One additional constraint: You must use a Dictionary in
#  the solution.

#  Student's Name: Trey Everson

#  Student's UT EID: RHE 323

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 9/9/19

#  Date Last Modified:


def search(name, dict):
    return name in dict


def decreasing(a):
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = 1001
    for i in range(1, len(a)):
        if a[i] >= a[i-1]:
            return False
    return True


def increasing(a):
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = 1001
    for i in range(1, len(a)):
        if a[i] <= a[i-1]:
            return False
        return True


def data_one_name(name, dict):
    return dict[name]


def one_decade(dict, decade):
    list = []
    decade = decade % 1900 // 10
    for key in dict:
        count = 0
        for rank in dict[key]:
            if rank == 0:
                count += 1
            if (count == 10) and (dict[key][decade] != 0):
                list.append(key)
        list.sort()
        return list


def all_decades(dict):
    list = []
    for key in dict:
        if 0 not in dict[key]:
            list.append(key)
        list.sort()
        return list


def all_rank(dict, decade):
    list = []
    decade = (decade % 1900) // 10
    for name in dict:
        if dict[name][decade] != 0:
            list.append(name)
    list.sort()
    return list


def more_popular(dict):
    list = []
    for name in dict:
        if decreasing(dict[name]):
            list.append(name)
    for i in range(len(dict[name])):
        if dict[name][i] == 1001:
            dict[name][i] = 0
    list.sort()
    return list


def less_popular(dict):
    list = []
    for name in dict:
        if increasing(dict[name]):
            list.append(name)
    for i in range(len(dict[name])):
        if dict[name][i] == 1001:
            dict[name][i] = 0
    list.sort()
    return list


def highest_rank(name, dict):
    max = 1000
    for rank in dict[name]:
        if rank < max and rank != 0:
            max = rank
            index = dict[name].index(rank)
    return 1900 + (index * 10)


def main():
    d = {}

    names = open('names.txt', 'r')

    # Fills dictionary with data from names.txt; name is key, list of rankings for each decade is value
    for line in names:
        name, d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10 = line.split(' ')
        rankings = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]
        for i in range(len(rankings)):
            rankings[i] = int(rankings[i])
        d[name] = rankings

    names.close()

    while True:
        print("Options:\n"
              "Enter 1 to search for names.\n"
              "Enter 2 to display data for one name.\n"
              "Enter 3 to display all names that appear in only one decade.\n"
              "Enter 4 to display all names that appear in all decades.\n"
              "Enter 5 to display all names that are more popular in every decade.\n"
              "Enter 6 to display all names that are less popular in every decade.\n"
              "Enter 7 to quit.\n")
        choice = int(input("Enter choice: "))
        # option 1
        if choice == 1:
            name = str(input("Enter a name: "))
            if search(name, d):
                print('\nThe matches with their highest ranking decade are:')
                print(name, str(highest_rank(name, d)))
            else:
                print(name, "does not appear in any decade.")
            print()
        # option 2
        elif choice == 2:
            name = str(input("Enter a name: "))
            if search(name, d):
                ranks = data_one_name(name, d)
                print(name + ': ' + ' '.join(str(i) for i in ranks))
                index = 0
                for i in range(1900, 2010, 10):
                    print(str(i) + ': ' + str(ranks[index]))
                    index += 1
            else:
                print(name, "does not appear in any decade.")
            print()
        # option 3
        elif choice == 3:
            decade = int(input("Enter a decade: "))
            print("The names are in alphabetical: ")
            names_list = one_decade(d, decade)
            print(decade)
            for name in names_list:
                print(name)
            print()
        elif choice == 4:
            names_list = all_decades(d)
            print(len(names_list), "names appear in every decade. The names are:")
            for name in names_list:
                print(name)
            print()
        elif choice == 5:
            names_list = decreasing(d)
            print(str(len(names_list)) + "names are more popular in every decade.")
            for name in names_list:
                print(name)
            print()
        elif choice == 6:
            names_list = decreasing(d)
            print(str(len(names_list)) + " names are less popular in every decade.")
            for name in names_list:
                print(name)
            print()
        elif choice == 7:
            print("\nGoodbye.")
            break


main()
