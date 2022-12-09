from typing import Tuple


map_selected = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}


points_by_selected = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

win_by_selected = {
    'X': 'Z',
    'Y': 'X',
    'Z': 'Y'
}

lose_by_selected = {
    'X': 'Y',
    'Y': 'Z',
    'Z': 'X'
}


def map_by_selected(line: str) -> Tuple[str, str]:
    selected_by_player = line.split()
    return map_selected[selected_by_player[0]], selected_by_player[1]


def get_calculate_selected(selected_by_player: Tuple[str, str]) -> Tuple[int, int]:
    return points_by_selected[selected_by_player[0]], points_by_selected[selected_by_player[1]]


def get_calculate_round_played(selected_elf: str) -> Tuple[int, int]:
    score_player, score_elf = 0, 0
    if selected_elf == 'Y':
        score_player, score_elf = 3, 3
    elif selected_elf == 'X':
        score_player = 6
    elif selected_elf == 'Z':
        score_elf = 6
    return score_player, score_elf

def transform_selected(selected_player: str, selected_elf: str) -> Tuple[str, str]:
    selected_final = selected_elf
    if selected_elf == 'Y':
        selected_final = selected_player
    elif selected_elf == 'X':
        selected_final = win_by_selected[selected_player]
    elif selected_elf == 'Z':
        selected_final = lose_by_selected[selected_player]
    return selected_player, selected_final

def score_round(selected_by_player: Tuple[str, str]) -> Tuple[int,int]:
    score_round_played = get_calculate_round_played(selected_by_player[1])
    selected_by_player_final = transform_selected(*selected_by_player)
    score_player, score_elf = get_calculate_selected(selected_by_player_final)
    score_player += score_round_played[0]
    score_elf += score_round_played[1]
    return score_player, score_elf


def calculate_score(filename: str) -> Tuple[int, int]:
    score_player, score_elf = 0, 0
    for line in open(filename, mode='r'):
        selected_by_player = map_by_selected(line)
        score = score_round(selected_by_player)
        score_player += score[0]
        score_elf += score[1]
    return score_player, score_elf


score = calculate_score('input.txt')
print(score[1])
