def get_array(file_name: str):
    with open(file_name) as f:
        array = [[int(x) for x in line.split(",")] for line in f]
    return(array)

def max_exp(arr: list):
    '''find the maximum base exponent pair in array
    array is a list of lists
    '''
    new_arr = arr.copy()
    for pair in arr:
        for pair2 in arr:
            if pair2[0] > pair[0] and pair2[1] > pair[1]:
                new_arr.remove(pair)
                break
    return new_arr

if __name__ == "__main__":
    exponents = get_array('p099_base_exp.txt')
    print("length is: ", len(exponents))
    print(len(max_exp(exponents)))