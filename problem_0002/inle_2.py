def problem2():
    sum = 0
    fib1 = 1
    fib2 = 1
    fib3 = None

    while fib2 < 4000000:
        if fib2 % 2 == 0:
            sum += fib2
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3

    return sum


print(problem2())
