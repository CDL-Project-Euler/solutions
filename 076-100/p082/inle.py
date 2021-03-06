from copy import deepcopy


def min_path_sum2(array: list) -> int:
    """Return minimum sum of path from left side to right."""
    min_array = deepcopy(array)
    for x in range(1, len(array[0])):
        min_array[0][x] += min_array[0][x-1]
        for y in range(1, len(array)):
            min_array[y][x] += min(min_array[y][x-1], min_array[y-1][x])

        for y in range(len(array)-2, -1, -1):
            min_array[y][x] = min(min_array[y][x], array[y][x] + min_array[y+1][x])

    minimum = min_array[0][-1]
    for y in range(1, len(array)):
        minimum = min(minimum, min_array[y][-1])
    return minimum


if __name__ == "__main__":
    with open("82_input.txt") as f:
        array = [list(map(int, line.split(","))) for line in f]
    print(min_path_sum2(array))
