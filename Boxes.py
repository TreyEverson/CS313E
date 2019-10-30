#  File: Boxes.py

#  Description: Find largest set of nesting boxes 

#  Student Name: Trey Everson

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: 10/13/2019

#  Date Last Modified: 10/16/2019

# function returns if one box fits in another

def box_fits(box1, box2):
    if (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2]):
        return 1
    else:
        return 0

# recursively get all of the paths for a val
def get_paths (dictionary, val):
    if dictionary[val] == []:
        return [[val]]
    else:
        ret = []
        for i in dictionary[val]:
            temp = get_paths(dictionary, i)
            for path in temp:
                ret.append(path)
        for path in ret:
            path.insert(0, val)
        return ret

def main():
    in_file = open('./boxes.txt', 'r')
    total_boxes = in_file.readline()
    total_boxes = total_boxes.strip()
    total_boxes = int(total_boxes)

    boxes = []
    # add all of the boxes to a 2D list
    while total_boxes > 0:
        line = in_file.readline()
        line = line.strip()
        line = line.split()
        for i in range (len(line)):
            line[i] = int(line[i])
        line = sorted(line)
        line = tuple(line)
        boxes.append(line)
        total_boxes -=1
    boxes = sorted(boxes)


    # create a dictionary with the box as the value and all boxes greater than it
    # as the value
    box_inside = []
    #number of bigger boxes
    num_fits = 0
    dict_bigger_boxes = {}
    for i in range(0,len(boxes)):
        for j in range(0,len(boxes)):
            if i == j:
                continue
            if box_fits(boxes[i], boxes[j]) == 1:
                box_inside.append(boxes[j])
        dict_bigger_boxes[boxes[i]] = (box_inside)
        # reset the values
        box_inside = []
        num_fits = 0
    all_paths = []
    i = 0
    try:
        minimums = []
        minimums.append(boxes[0])
        # determine which boxes can be the first box in the sequence
        for i in range(1,len(boxes)):
            if box_fits(boxes[0],boxes[i])==0:
                minimums.append(boxes[i])
            else:
                continue
        for i in range(0,len(minimums)):
            cur = get_paths(dict_bigger_boxes, minimums[i])
            for j in cur:
                all_paths.append(j)


        # determine the maximum cycle length
        maximum = 0
        all_final_paths = []
        for i in range(0,len(all_paths)):
            if len(all_paths[i]) >= maximum:
                maximum = len(all_paths[i])
            else:
                continue
        # figure out all path(s) equal to the cycle length
        for i in range(0,len(all_paths)):
            if len(all_paths[i]) >= maximum:
                all_final_paths.append(all_paths[i])
            else:
                continue
        print('Largest Subset of Nesting Boxes')
        for i in range (0,len(all_final_paths)):
            for j in range(0,len(all_final_paths[i])):
                print(list(all_final_paths[i][j]))
            print()
    except:
        print('No Nesting Boxes')


main()
