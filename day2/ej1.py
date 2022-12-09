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


def map_by_selected(line: str) -> Tuple[str, str]:
    selected_by_player = line.split()
    return map_selected[selected_by_player[0]], selected_by_player[1]


def get_calculate_round_played(selected_player: str, selected_elf: str) -> Tuple[int, int]:
    score_player, score_you = 0, 0
    if selected_player == selected_elf:
        score_player, score_you = 3, 3
    elif win_by_selected[selected_player] == selected_elf:
        score_player = 6
    elif win_by_selected[selected_elf] == selected_player:
        score_you = 6
    return score_player, score_you


def get_calculate_selected(selected_by_player: Tuple[str, str]) -> Tuple[int, int]:
    return points_by_selected[selected_by_player[0]], points_by_selected[selected_by_player[1]]


def score_round(selected_by_player: Tuple[str, str]) -> Tuple[int,int]:
    score_player, score_you = get_calculate_selected(selected_by_player)
    score_round_played = get_calculate_round_played(*selected_by_player)
    score_player += score_round_played[0]
    score_you += score_round_played[1]
    return score_player, score_you


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
