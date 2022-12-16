"""
Advent of Code 2022, Day 8
solution by Maja Sellmer
"""

import numpy as np

with open('advent8.txt') as trees:
    trees_grid = trees.readlines()
    grid_size = len(trees_grid)
    for i in range(grid_size):
        this_line = list(trees_grid[i].rstrip("\n"))
        this_line = [int(x) for x in this_line]
        trees_grid[i] = this_line
    # # initialize all trees as invisible
    # visible_grid = np.zeros([grid_size, grid_size], dtype=int)
    # # those on the edge are visible from the outside
    # visible_grid[0] = np.ones(grid_size, dtype=int)
    # visible_grid[-1] = np.ones(grid_size, dtype=int)
    # for i in range(grid_size):
    #     visible_grid[i][0] = 1
    #     visible_grid[i][-1] = 1
    # # go through all rows and columns
    # # mark trees as visible if they are taller than the current max
    # for i in range(grid_size):
    #     row_max = 0
    #     for j in range(grid_size):
    #         if trees_grid[i][j] > row_max:
    #             visible_grid[i][j] = 1
    #             row_max = trees_grid[i][j]
    # for j in range(grid_size):
    #     column_max = 0
    #     for i in range(grid_size):
    #         if trees_grid[i][j] > column_max:
    #             visible_grid[i][j] = 1
    #             column_max = trees_grid[i][j]
    # for i in range(grid_size):
    #     row_max = 0
    #     for j in range(grid_size-1, -1, -1):
    #         if trees_grid[i][j] > row_max:
    #             visible_grid[i][j] = 1
    #             row_max = trees_grid[i][j]
    # for j in range(grid_size):
    #     column_max = 0
    #     for i in range(grid_size-1, -1, -1):
    #         if trees_grid[i][j] > column_max:
    #             visible_grid[i][j] = 1
    #             column_max = trees_grid[i][j]
    # visible_sum = 0
    # for i in range(grid_size):
    #     for j in range(grid_size):
    #         visible_sum += visible_grid[i][j]
    # print(visible_sum)
    # initialize all viewing distances as 1
    viewing_distances = np.ones([grid_size, grid_size, 4], dtype=int)
    # for each tree in the grid, calculate viewing distance in all four directions
    # for points on the edge, set viewing distance to 0
    for i in range(grid_size):
        for j in range(grid_size):
            for x in range(i-1, 0, -1):
                if trees_grid[x][j] >= trees_grid[i][j]:
                    break
                viewing_distances[i][j][0] += 1
            if i == 0:
                viewing_distances[i][j][0] = 0
            for x in range(i+1, grid_size-1):
                if trees_grid[x][j] >= trees_grid[i][j]:
                    break
                viewing_distances[i][j][1] += 1
            if i == grid_size-1:
                viewing_distances[i][j][1] = 0
            for y in range(j-1, 0, -1):
                if trees_grid[i][y] >= trees_grid[i][j]:
                    break
                viewing_distances[i][j][2] += 1
            if j == 0:
                viewing_distances[i][j][2] = 0
            for y in range(j+1, grid_size-1):
                if trees_grid[i][y] >= trees_grid[i][j]:
                    break
                viewing_distances[i][j][3] += 1
            if j == grid_size-1:
                viewing_distances[i][j][3] = 0
    # calculate scenic scores for all points and find maximum
    max_scenic_score = 0
    for i in range(grid_size):
        for j in range(grid_size):
            scenic_score = 1
            for k in range(4):
                scenic_score *= viewing_distances[i][j][k]
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    print(max_scenic_score)
