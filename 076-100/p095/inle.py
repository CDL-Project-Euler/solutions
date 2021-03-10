def solve(limit: int):
    """Solve project euler problem 95."""
    sum_divs = [1] * (limit + 2)  # Stores sum of proper divisors
    amicables = {1}  # Max numbers in amicable chains
    max_length = 0
    max_list_min = None

    for i in range(2, limit + 1):
        # As only sums up to i calculated, only chains starting with greatest member followed
        sum_proper = chain_min = i
        length = 1
        while (sum_proper := sum_divs[sum_proper]) <= i and sum_proper not in amicables:
            if sum_proper == i:
                amicables.add(i)
                if length > max_length:
                    max_length = length
                    max_list_min = chain_min
                break
            chain_min = min(chain_min, sum_proper)
            length += 1

        for j in range(2 * i, limit + 1, i):
            sum_divs[j] += i
    print(max_list_min)

if __name__ == "__main__":
    solve(1000000)
