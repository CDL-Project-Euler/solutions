def polygonal(s: int, n: int) -> int:
    """Return the nth s-gonal number."""
    return ((s - 2) * n * n - (s - 4) * n) // 2


def cycle(suffix: int, types: set, prefix: int, P: list):
    """Construct set of polygonal numbers recursively."""
    if not types:  # If all polygonal types are represented in set
        if suffix == prefix:  # Prefix of first number must equal last suffix
            return suffix
        return None

    for side in types:
        types.remove(side)
        for new_suffix in P[side][suffix - 10]:  # Loops through suffixes for given prefix
            if new_suffix > 9:  # Prefix of next must be 2 digits
                answer = cycle(new_suffix, types, prefix, P)  # Outputs None if no solution in branch
                if answer is not None:
                    return (suffix, answer)
        types.add(side)
    return None


def solve():
    """Solve Project Euler Problem 61."""
    # List contains suffix lists for each prefix for each polygonal type
    P = [[[] for _ in range(90)] for _ in range(7)]
    n = 1
    is_not_finished = True
    while is_not_finished:
        is_not_finished = False
        for s in range(3, 9):  # Loops through polygonal types
            val = polygonal(s, n)
            if 1000 <= val < 10000:
                P[s - 3][val // 100 - 10].append(val % 100)
            if val < 10000:
                is_not_finished = True
        n += 1

    # Loops through all triangle numbers and finds all branches
    output = None
    for i in range(len(P[0])):
        prefix = i + 10
        for suffix in P[0][i]:
            if (output := cycle(suffix, set(range(1, 6)), prefix, P)):
                output = (prefix, output)
                break
        if output:
            break
    print(output)
    #  Outputs (82, (56, (25, (12, (81, (28, 82))))))
    #  print(8256 + 5625 + 2512 + 1281 + 8128 + 2882) -> 28684


solve()
