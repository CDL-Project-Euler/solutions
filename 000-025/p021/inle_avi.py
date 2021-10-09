def problem_21(limit: int):
    divisor_sums = [0] * (limit + 1)
    for divisor in range(1, limit):
        for divisor_multiple in range(2 * divisor, limit + 1, divisor):
            divisor_sums[divisor_multiple] += divisor

    sum_amicables = 0
    for i in range(2, limit):
        if i != divisor_sums[i] < limit + 1 and divisor_sums[divisor_sums[i]] == i:
            sum_amicables += i
    return sum_amicables

print(problem_21(10000000))