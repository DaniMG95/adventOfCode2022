from collections import deque
from typing import Tuple


def read_files(file, directories, size_directories):
    directory = '/'.join(directories)
    size_directories[directory] = []
    for line in file:
        line = line.rstrip('\n')
        if line[0] == '$':
            return line
        else:
            if 'dir' in line:
                size_directories[directory].append(directory + '/' + line.split(" ")[1])
            else:
                size_directories[directory].append(line.split(" ")[0])


def run_instruction(line, file, directories: deque, size_directories: dict) -> None:
    if not line:
        return None
    elif 'cd ..' in line:
        directories.pop()
    elif 'cd /' in line:
        directories.clear()
        directories.append('/')
    elif 'cd' in line:
        directories.append(line.split(' ')[2])
    elif 'ls' in line:
        line = read_files(file, directories, size_directories)
        run_instruction(line, file, directories, size_directories)


def calculate_size_by_key(key, size_directories: dict):
    size = 0
    for value in size_directories[key]:
        if value.isdigit():
            size += int(value)
        else:
            size += calculate_size_by_key(value, size_directories)
    return size


def calculate_size(size_directories: dict):
    size_directories_final = {}
    for key in size_directories.keys():
        size = calculate_size_by_key(key, size_directories)
        size_directories_final[key] = size
    return size_directories_final.values()


def get_directory(filename: str) -> Tuple[int, int]:
    directories = deque()
    size_directories = {}
    with open(filename) as file:
        for line in file:
            run_instruction(line.rstrip('\n'), file, directories, size_directories)
    directories_size = calculate_size(size_directories)
    directories_small = sum(filter(lambda x: x < 100000, directories_size))
    directory_delete = min(filter(lambda x: x >= (30000000 - (70000000 - max(directories_size))), directories_size))
    return directories_small, directory_delete


print(get_directory('input.txt'))



