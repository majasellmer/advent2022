"""
Advent of Code 2022, Day 3
solution by Maja Sellmer
"""

with open('advent3.txt') as rucksacks:
    rucksacks_list = [line.rstrip("\n") for line in rucksacks.readlines()]
    rucksacks_compartments = []
    rucksacks_items = []
    # separate each rucksack in two compartments
    for rucksack in rucksacks_list:
        first_half = rucksack[:len(rucksack)//2]
        second_half = rucksack[len(rucksack)//2:]
        rucksacks_compartments.append([first_half, second_half])
        # check which item appears in both compartments
        for item in first_half:
            if item in second_half:
                rucksacks_items.append(item)
                break
    badges = []
    group = 0
    # separate the elves into groups of three
    while group < len(rucksacks_list)//3:
        first_member = rucksacks_list[3*group]
        second_member = rucksacks_list[3*group+1]
        third_member = rucksacks_list[3*group+2]
        # find their badge (the item they have in common)
        for char in first_member:
            if (char in second_member) and (char in third_member):
                badge = char
        badges.append(badge)
        group += 1
    priorities_dict = {}
    for char in "abcdefghijklmnopqrstuvwxyz":
        priorities_dict[char] = ord(char) - 96
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        priorities_dict[char] = ord(char) - 38
    # items_priorities_sum = 0
    # for item in rucksacks_items:
    #     items_priorities_sum += priorities_dict.get(item)
    # print(items_priorities_sum)
    badges_priorities_sum = 0
    for badge in badges:
        badges_priorities_sum += priorities_dict.get(badge)
    print(badges_priorities_sum)
