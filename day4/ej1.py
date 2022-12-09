from typing import List, Tuple


def detect_solapion(pair: List) -> bool:
    section_1 = set(range(pair[0][0], pair[0][1]+1))
    section_2 = set(range(pair[1][0], pair[1][1] + 1))
    return section_1.issubset(section_2) or section_2.issubset(section_1)

def transform_pairs(pair: str) -> List:
    transform = [pairs.split('-') for pairs in pair.split(',')]
    for i in range(len(transform)):
        transform[i] = list(map(int, transform[i]))
    return transform


def detect_solapion_v2(pair: List) -> bool:
    section_1 = set(range(pair[0][0], pair[0][1]+1))
    section_2 = set(range(pair[1][0], pair[1][1] + 1))
    return bool(section_1.intersection(section_2))


def fully_contains(filename: str) -> Tuple[int, int]:
    cnt = 0
    cnt_v2 = 0
    with open(filename) as file:
        for line in file:
            pair = transform_pairs(line.rstrip('\n'))
            if detect_solapion(pair):
                cnt += 1
            if detect_solapion_v2(pair):
                cnt_v2 += 1
    return cnt, cnt_v2

print(fully_contains('input.txt'))
