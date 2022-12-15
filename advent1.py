"""
Advent of Code 2022, Day 1
solution by Maja Sellmer
"""

with open('advent1.txt') as calories:
    calories_list = calories.readlines()
    calories_per_elf = []
    counter = 0
    current_elf = []
    # go through calories list, dividing it into individual lists for each elf
    while calories_list != []:
        # two elves are separated by an empty line
        if calories_list[0] == "\n":
            calories_per_elf.append(current_elf)
            counter += 1
            current_elf = []
        else:
            current_elf.append(int(calories_list[0].rstrip('\n')))
        calories_list.pop(0)
    calories_per_elf_sums = []
    # go through the list and calculate the calories sum for each elf
    for elf in calories_per_elf:
        sum_current_elf = 0
        for food in elf:
            sum_current_elf += food
        calories_per_elf_sums.append(sum_current_elf)
    # sort the list so the elf with the most calories is first
    calories_per_elf_sums.sort(reverse=True)
    # print sum of calories of the top elf / top three elves
    # print(calories_per_elf_sums[0])
    print(calories_per_elf_sums[0]+calories_per_elf_sums[1]+calories_per_elf_sums[2])
    