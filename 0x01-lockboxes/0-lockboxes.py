#!/usr/bin/python3
""" lockboxes module"""


def canUnlockAll(boxes):
    """canUnlockAll: determines if all the boxes can be opened by the provided keys.
    """
    n = len(boxes)
    opened_boxes = set([0])  # Start with the first box opened
    stack = [0]  # Start exploring from the first box

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in opened_boxes and key < n:
                opened_boxes.add(key)
                stack.append(key)

    return len(opened_boxes) == n

