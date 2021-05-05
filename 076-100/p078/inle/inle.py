class Solution:
    def __init__(self, search_range: int, divisor: int):
        self.search_range = search_range
        self.counts = [[0] * search_range for _ in range(search_range)]
        self.divisor = divisor
        for i in range(search_range):
            if (answer := self.p(i, i)) == 0:
                print(i, ":", answer)
                break
            # print(i, ":", answer)

    def p(self, maximum: int, n: int):
        """Count ways to split n items with groups of max size, maximum."""
        if n == 0:
            return 1
        if self.counts[maximum-1][n-1]:
            return self.counts[maximum-1][n-1]
        solution = 0
        for i in range(1, min(n + 1, maximum + 1)):
            solution = (solution + self.p(i, n - i)) % self.divisor
        self.counts[maximum-1][n-1] = solution
        return solution


Solution(10000, 10000)  # 100000 greater than 2000 need faster method --> check out euler video
