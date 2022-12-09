from typing import Tuple


def get_compartiments(items: str) -> Tuple[str, str]:
    half = int(len(items)/2)
    return items[:half], items[half:]


def get_duplicated(items: Tuple[str, str]) -> str:
    for char in items[0]:
        if char in items[1]:
            return char

def get_priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


def calculate_priority(filename: str) -> int:
    priority = 0
    with open(filename, mode='r') as file:
        for line in file:
            items = get_compartiments(line.rstrip('\n'))
            item = get_duplicated(items)
            priority += get_priority(item)
    return priority


priority = calculate_priority('input.txt')
print(priority)