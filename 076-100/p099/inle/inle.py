from math import log
def get_array(file_name: str):
    with open(file_name) as f:
        array = [[int(x) for x in line.split(",")] for line in f]
    return(array)

def max_exp(arr: list):
    '''find the maximum base exponent pair in array
    array is a list of lists
    '''
    line_max = 0 # Index of arr containing largest base-exponent pair
    for i in range(1, len(arr)):
        if arr[i][0] ** (arr[i][1] / arr[line_max][1]) > arr[line_max][0]:
            line_max = i
            print("new line max", i)
    return line_max + 1

if __name__ == "__main__":
    exponents = get_array('p099_base_exp.txt')
    print("length is: ", len(exponents))
    print(max_exp(exponents))