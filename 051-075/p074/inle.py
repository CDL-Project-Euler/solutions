def solve(limit: int):
    """Solve project euler problem 74."""
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    cycle3 = {169, 1454, 363601}
    cycle2 = {871, 872, 45361, 45362}
    count = 0
    for i in range(1, limit):
        dig_fact = i
        length = 1
        while length <= 61:  # Follow dig-fact
            if dig_fact == (dig_fact := sum(map(factorials.__getitem__, map(int, str(dig_fact))))):
                break
            if dig_fact in cycle2:
                length += 2
                break
            if dig_fact in cycle3:
                length += 3
                break
            length += 1
        if length == 60:
            count += 1
    return count


if __name__ == "__main__":
    print(solve(1000000))
