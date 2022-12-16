"""
Advent of Code 2022, Day 5
solution by Maja Sellmer
"""

with open('advent5.txt') as supply_stacks:
    supply_stacks_list = supply_stacks.readlines()
    # separate input into starting configuration and list of movements
    for i in range(len(supply_stacks_list)):
        if supply_stacks_list[i] == "\n":
            starting_configuration = supply_stacks_list[:i]
            movements_list = supply_stacks_list[i+1:]
    # stack numbers are in the last line of starting configuration
    stack_nums = starting_configuration[-1].lstrip(" ").rstrip(" \n").split("   ")
    stack_nums = [int(x) for x in stack_nums]
    stacks = [[] for num in stack_nums]
    # from the bottom up, add the crates onto the stacks
    for i in range(2, len(starting_configuration)+1):
        this_line = starting_configuration[-i].rstrip("\n")
        for n in stack_nums:
            if this_line[4*n-3] != " ":
                stacks[n-1].append(this_line[4*n-3])
    movements = []
    # from each movement, extract the relevant data:
    # num of stacks to be moved, starting stack, destination stack
    for movement in movements_list:
        movement = movement.rstrip("\n")
        for char in 'movefromto':
            movement = movement.replace(char, '')
        movement = movement.lstrip(" ").split("  ")
        movement = [int(x) for x in movement]
        movements.append(movement)
    # execute all the movements
    for movement in movements:
        # for i in range(movement[0]):
        #     r = len(stacks[movement[1]-1])-1
        #     moving = stacks[movement[1]-1].pop(r)
        #     stacks[movement[2]-1].append(moving)
        for i in range(-movement[0], 0):
            moving = stacks[movement[1]-1].pop(i)
            stacks[movement[2]-1].append(moving)
    top_elements = [stack[-1] for stack in stacks]
    print(''.join(top_elements))
