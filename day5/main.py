from collections import deque
from typing import List, Tuple
from copy import deepcopy

def structure_stacks(file: str) -> List:
    stacks_data = []
    for line in file:
        if line == '\n':
            break
        else:
            stacks_data.append(line.rstrip('\n'))
    stacks = [deque() for _ in range(int(stacks_data[-1].strip()[-1]))]
    for line in stacks_data[::-1][1:]:
        for idx, i in enumerate(list(range(0, len(line), 4))):
            value = line[i:i+4]
            if '[' in value:
                stacks[idx].append(value.strip()[1])
    return stacks


def transform_instruction(line: str) -> Tuple[int, int, int]:
    data = line.split()
    mov = int(data[1])
    location = int(data[3])
    to_location = int(data[5])
    return mov, location, to_location


def execute_instruction(stacks: List, instruction: Tuple) -> None:
    for _ in range(instruction[0]):
        stacks[instruction[2]-1].append(stacks[instruction[1]-1].pop())


def execute_instruction_v2(stacks: List, instruction: Tuple) -> None:
    item_move = [stacks[instruction[1]-1].pop() for _ in range(instruction[0])]
    for item in item_move[::-1]:
        stacks[instruction[2]-1].append(item)


def rearrangement(filename: str) -> Tuple[List, List]:
    with open(filename) as file:
        stacks = structure_stacks(file)
        stacks_v2 = deepcopy(stacks)
        for line in file:
            instruction = transform_instruction(line)
            execute_instruction(stacks, instruction)
            execute_instruction_v2(stacks_v2, instruction)
        return stacks, stacks_v2


stacks, stacks_v2 = rearrangement('input.txt')
# for i in range(len(stacks)):
#     print(stacks[i].pop(), end='')
for i in range(len(stacks_v2)):
    print(stacks_v2[i].pop(), end='')

