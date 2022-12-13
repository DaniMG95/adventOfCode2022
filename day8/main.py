from typing import List


def is_visible_tree(coord_x: int, coord_y: int, trees: List) -> bool:
    n_trees = len(trees[0])
    height = int(trees[coord_y][coord_x])
    if coord_x == 0 or coord_x == n_trees or coord_y == 0 or coord_y == len(trees):
        return True

    top = any([height <= int(trees[i][coord_x]) for i in range(0, coord_y)])
    bottom = any([height <= int(trees[i][coord_x]) for i in range(coord_y+1, len(trees))])
    left = any([height <= int(trees[coord_y][i]) for i in range(0, coord_x)])
    right = any([height <= int(trees[coord_y][i]) for i in range(coord_x+1, n_trees)])

    return not all([top, bottom, left, right])


def scenic_score(coord_x: int, coord_y: int, trees: List) -> int:
    n_trees = len(trees[0])
    height = int(trees[coord_y][coord_x])
    top = [height > int(trees[i][coord_x]) for i in range(coord_y-1, -1, -1)]
    bottom = [height > int(trees[i][coord_x]) for i in range(coord_y + 1, len(trees))]
    left = [height > int(trees[coord_y][i]) for i in range(coord_x-1, -1, -1)]
    right = [height > int(trees[coord_y][i]) for i in range(coord_x + 1, n_trees)]

    top = top.index(False)+1 if False in top else len(top)
    bottom = bottom.index(False)+1 if False in bottom else len(bottom)
    left = left.index(False)+1 if False in left else len(left)
    right = right.index(False)+1 if False in right else len(right)

    return top * bottom * left * right




def prepare_data(file) -> List:
    return [line.rstrip('\n') for line in file]


def get_visible_trees(filename: str) -> int:
    with open(filename) as file:
        trees = prepare_data(file)
    return sum([is_visible_tree(i, j, trees) for i in range(0, len(trees[0])) for j in range(0, len(trees))])


def get_max_score(filename: str) -> int:
    with open(filename) as file:
        trees = prepare_data(file)
    return max([scenic_score(i, j, trees) for i in range(0, len(trees[0])) for j in range(0, len(trees))])



print(get_visible_trees('input.txt'))
print(get_max_score('input.txt'))