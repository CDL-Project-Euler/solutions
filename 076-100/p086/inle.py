def solve(to_exceed: int):
    solutions = 0
    z = 0
    while solutions <= to_exceed:
        z += 1
        for a in range(2, 2 * z + 1):
            if ((a * a + z * z) ** 0.5) % 1 == 0:
                solutions += a // 2 - max(0, a - z - 1)
    print(z)


if __name__ == "__main__":
    solve(1000000)