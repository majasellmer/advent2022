"""
Advent of Code 2022, Day 6
solution by Maja Sellmer
"""

with open('advent6.txt') as tuning:
    datastream_list = tuning.readlines()
    datastream = datastream_list[0].rstrip("\n")
    # n = 4
    n = 14
    index = n
    potential_marker = datastream[:n]
    while True:
        # stop when string of n different characters found
        if len(set(potential_marker)) == n:
            break
        potential_marker = potential_marker[1:]+datastream[index]
        index += 1
    print(index)
  