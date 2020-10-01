from math import log

def length_num_digits(number: int):
    return(int(log(number, 10))+ 1)

def sqrt_iteration(num: int, denom: int):
    return 2*denom + num , num + denom

def square_root_convergence(num_expansion):
    count = 0
    num = 1
    denom = 1
    for _ in range(num_expansion):
        num, denom = sqrt_iteration(num, denom)
        if length_num_digits(num) > length_num_digits(denom):
            count += 1
    return count

if __name__ == "__main__":
    print(square_root_convergence(1000))
