#!/usr/bin/python3
def pascal_triangle(n):
    """
    """
    if n <= 0 :
        return []
    
    if n == 1:
        return [[1]]
    else: 
        result = pascal_triangle(n - 1)
    row = [1]
    prev= result[-1]
    for i in range(len(prev) - 1):
        row.append(prev[1] + prev[i+1])
    row += [1]
    result.append(row)
    return result
        