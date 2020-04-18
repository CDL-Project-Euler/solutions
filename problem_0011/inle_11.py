def get_array(file_name: str):
    with open(file_name) as f:
        array = [[int(x) for x in line.split()] for line in f]
    return(array)


def prod_vert_lines(grid: list, line_size: int):
    height = len(grid)
    width = len(grid[1])
    max_sum = 1
    count = 0
    for indexy in range(height - line_size + 1):
        for indexx in range(width):
            current = 1
            for y in range(indexy, indexy + line_size):
                current *= grid[y][indexx]
            max_sum = max(max_sum, current)
    
    return max_sum


def prod_horiz_lines(grid: list, line_size: int):
    height = len(grid)
    width = len(grid[1])
    max_sum = 1

    for indexy in range(height):
        for indexx in range(width-line_size + 1):
            current = 1
            for x in range(indexx, indexx + line_size):
                current *= grid[indexy][x]
            max_sum = max(max_sum, current)
    return max_sum


def prod_downdiag_lines(grid: list, line_size: int):
    height = len(grid)
    width = len(grid[1])
    max_sum = 1

    for indexy in range(height - line_size + 1):
        for indexx in range(width-line_size + 1):
            current = 1
            for y in range(line_size):
                current *= grid[indexy+ y][indexx + y]
            max_sum = max(max_sum, current)
    return max_sum


def prod_updiag_lines(grid: list, line_size: int):
    height = len(grid)
    width = len(grid[1])
    max_sum = 0

    for indexx in range(width-line_size+1):
        for indexy in range(line_size+1, height):
            current = 1
            for i in range(line_size):
                current *= grid[indexy-i][(indexx+i)]
            max_sum = max(max_sum, current)
    return max_sum


def problem_11():
    array = get_array("11_input.txt")
    line_size = 4
    print(max(prod_updiag_lines(array, line_size), prod_downdiag_lines(array, line_size), prod_horiz_lines(array, line_size), prod_vert_lines(array, line_size)))

if __name__ == "__main__":
    problem_11()


