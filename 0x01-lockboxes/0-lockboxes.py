#!/usr/bin/python3
""" Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False"""
from collections import deque


def canUnlockAll(boxes):
    n = len(boxes)
    if n == 0:
        return False

    opened = set()
    opened.add(0)

    queue = deque([0])

    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if key < n and key not in opened:
                opened.add(key)
                queue.append(key)

    return len(opened) == n
