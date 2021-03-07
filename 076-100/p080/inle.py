import decimal


def sum_sqrt_decs(num: int) -> int:
    """Sum first 100 decimals of the squareroot of num."""
    decimal.getcontext().prec = 103
    num = str(decimal.Decimal(num) ** decimal.Decimal(0.5)).replace(".", "")[:100]
    sum_digs = 0
    for i in range(len(num)):
        sum_digs += int(num[i])
    return sum_digs


def solve():
    """Solve project euler problem 80."""
    total = 0
    for i in range(1, 101):
        if (i ** 0.5) % 1 != 0:
            total += sum_sqrt_decs(i)
    print(total)


if __name__ == "__main__":
    solve()
