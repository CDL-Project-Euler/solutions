import math
import decimal

#didn't use
def length_num_digits(number: int):
    return(int(math.log(number, 10)))

def reciprocal_cycle_len(num: int):
    for index in range(1, 1000):
        remainder = (10**index) % num
        if remainder == 1:
            return index
        elif remainder == 0:
            return 0  #All number with no cycle
    return "later " #All numbers with cycles starting later

def max_reciprocal_cycles(maximum: int):
    #Not including maximum
    longest_cycle = 0
    longest = 0 #integer with longest_cycle

    for number in range(1, maximum):
        current_cycle = reciprocal_cycle_len(number)
        
        if current_cycle > longest_cycle:
            longest = number
            longest_cycle = current_cycle
    return longest_cycle, longest


if __name__ == "__main__":
    print(max_reciprocal_cycles(1000))