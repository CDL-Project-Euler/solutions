def get_array(file_name: str):
    with open(file_name) as f:
        array = [[int(x) for x in line.split()] for line in f]
    return(array)


def max_path_sum(array):
    for y_pos in range(1, len(array)):
        length = len(array[y_pos])
        for x_pos in range(length):
            if x_pos == 0:
                array[y_pos][0] += array[y_pos - 1][0]
            elif x_pos == length - 1:
                array[y_pos][x_pos] += array[y_pos - 1][-1]
            else:
                array[y_pos][x_pos] += max(array[y_pos-1][x_pos], array[y_pos-1][x_pos-1])
    return max(array[-1])

if __name__ == "__main__":
    array = get_array("18_input.txt")
    maximum = max_path_sum(array)
    print(maximum)
