def problem_28(size: int):
    #size must be odd
    sum_corners = 1
    x = 1
    for i in range(2, size+1, 2):
        sum_corners += 4 * x + 10 * i
        x += 4 * i
    return(sum_corners)

if __name__ == "__main__":
    print(problem_28(1001))
