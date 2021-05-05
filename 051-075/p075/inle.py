def gcf(m: int, n: int) -> int:
    """Find gcf of m and n."""
    while n:
        m, n = n, m % n
    return m


def solve(limit: int) -> int:
    """Solves project euler problem 75 with triangles up to limit."""
    multi_perims = set()
    single_perims = set()
    print((limit ** 0.5) // 2)
    for m in range(2, 1 + int((limit / 2) ** 0.5)):
        for n in range(1, m):
            if (perimeter := 2 * m * m + 2 * m * n) > limit:
                break
            if gcf(m, n) == 1 and m % 2 + n % 2 != 2:
                print(m * m - n * n, 2 * m * n, m * m + n * n, perimeter)
                for perim_mult in range(perimeter, limit + 1, perimeter):
                    if perim_mult not in multi_perims:
                        if perim_mult in single_perims:
                            single_perims.remove(perim_mult)
                            multi_perims.add(perim_mult)
                        else:
                            single_perims.add(perim_mult)
    print(single_perims)
    print(len(single_perims))


if __name__ == "__main__":
    solve(1500000)
