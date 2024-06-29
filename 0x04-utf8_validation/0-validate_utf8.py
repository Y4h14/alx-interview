#!/usr/bin/env python3
"""defines a fucntion that check if data is utf"""


def validUTF8(data: list) -> bool:
    """checks if the given data is UTF8 encoded

    Args:
        data (list): set containing multiple charecters

    Returns:
        bool: True if the data is in UTF8
    """
    count = 0
    for char in data:
        if count == 0:
            if (char >> 5) == 0b110:
                count = 1
            elif (char >> 4) == 0b1110:
                count = 2
            elif (char >> 3) == 0b11110:
                count = 3
            elif (char >> 7):
                return False
        else:
            if (char >> 6) != 0b10:
                return False
            count -= 1
        return count == 0
