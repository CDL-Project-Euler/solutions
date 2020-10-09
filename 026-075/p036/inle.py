def problem_36(maximum: int):
    sum_pals = 0
    for number in range(maximum):
        if number == int(str(number)[::-1]) and bin(number)[2:] == bin(number)[:1:-1]:
            print(number)
            sum_pals += number
    return sum_pals

if __name__ == "__main__":
    print(problem_36(1000000))