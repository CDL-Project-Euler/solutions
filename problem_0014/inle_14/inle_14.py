def length_collatz(number):
    count = 1
    while number > 1:
        if number%2 == 0:
            number = number/2
        else:
            number = 3 * number + 1
        count += 1
    return count

def longest_collatz(max):
    longest = 0
    length = 0
    for start in range(2, max):
        current_len = length_collatz(start)
        if length < current_len:
            length = current_len
            longest = start
    return longest

def optimized_collatz(max):
    bool_array = np.full(max, 0, dtype = int)



if __name__ == "__main__":
    print(longest_collatz(1000000))
