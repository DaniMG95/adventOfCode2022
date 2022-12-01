from typing import List

def calories_elfs(input: str) -> List[int]:
    calories = [0]
    for line in open(input, mode='r'):
        if line == '\n':
            calories.append(0)
        else:
            calories[-1] = calories[-1] + int(line)
    return calories


def max_calories(calories: List):
    return max(calories)

def max_calories_top3(calories: List):
    calories.sort(reverse=True)
    return sum(calories[0:3])



list_calories = calories_elfs("input.txt")

print(max_calories(list_calories))
print(max_calories_top3(list_calories))