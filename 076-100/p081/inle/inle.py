def get_array(file_name: str):
    with open(file_name) as f:
        array = [[int(x) for x in line.split(",")] for line in f]
    return(array)


def min_path_sum1(array):
    #row 0
    for x_pos in range(1, len(array[0])):
        array[0][x_pos] += array[0][x_pos - 1]

    #column 0
    for y_pos in range(1, len(array)):
        array[y_pos][0] += array[y_pos -1][0]

    #other rows
    for y_pos in range(1, len(array)):
        for x_pos in range(1, len(array[0])):
            array[y_pos][x_pos] += min(array[y_pos - 1][x_pos], array[y_pos][x_pos - 1])
    return array[-1][-1]

if __name__ == "__main__":
    array = get_array("81_input.txt")
    print(min_path_sum1(array))
