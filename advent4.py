"""
Advent of Code 2022, Day 4
solution by Maja Sellmer
"""

with open('advent4.txt') as assignments:
    assignments_list = assignments.readlines()
    assignment_pairs = []
    # get the endpoints of the intervals assigned
    for assignment in assignments_list:
        assignment_pair = assignment.rstrip("\n").split(',')
        assignment1 = [int(x) for x in assignment_pair[0].split('-')]
        assignment2 = [int(x) for x in assignment_pair[1].split('-')]
        assignment_pairs.append([assignment1, assignment2])
    full_overlap_counter = 0
    overlap_counter = 0
    # for each pair, check if there is full overlap / overlap
    for pair in assignment_pairs:
        [left1, right1] = pair[0]
        [left2, right2] = pair[1]
        if left1 <= left2 and right1 >= right2:
            full_overlap_counter += 1
        elif left1 >= left2 and right1 <= right2:
            full_overlap_counter += 1
        if left1 <= left2 <= right1:
            overlap_counter += 1
        elif left2 <= left1 <= right2:
            overlap_counter += 1
    print(full_overlap_counter)
    print(overlap_counter)
    