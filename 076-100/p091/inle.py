def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x

def solve(n: int) -> None:
    """Solve project euler problem 91 with x, y <= n."""
    count_triangles = 3 * n * n
    for x in range(1, n+1):
        for y in range(1, x+1):
            xy_gcd = gcd(x, y)
            move_x, move_y = x // xy_gcd, y // xy_gcd
            i = 1
            while y + i * move_x <= n and x - i * move_y >= 0:
                count_triangles += 1 + int(x != y)
                i += 1
            i = 1
            while y - i * move_x >= 0 and x + i * move_y <= n:
                count_triangles += 1 + int(x != y)
                i += 1
    print(count_triangles)


if __name__ == "__main__":
    solve(50)