from typing import List


def get_duplicated(items: List[str]) -> str:
    for char in items[0]:
        if char in items[1] and char in items[2]:
            return char


def get_priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


def calculate_priority(filename: str) -> int:
    priority = 0
    items_group = []
    with open(filename, mode='r') as file:
        for line in file:
            items_group.append(line.rstrip('\n'))
            if len(items_group) == 3:
                item = get_duplicated(items_group)
                priority += get_priority(item)
                items_group.clear()
    return priority


priority = calculate_priority('input.txt')
print(priority)
