#!/usr/bin/python3


def island_perimeter(grid):
    
    total = 0
    for i in range(0, len(grid)):
        for j in range (0, len(grid[i])):
            if grid[i][j] == 1:
                
                if grid[i-1][j] == 1 or grid[i][j-1] == 1:
                    total += 2
                else:
                    total += 4
            else:
                continue
    return total
