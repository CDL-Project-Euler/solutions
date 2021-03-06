'''
    Need to optimize the algorithm which counts all unique integer sums up to n, p(n)
    Could optimize space efficiency too...
'''
def p(limit: int, divisor: int) -> int:
    ways = [[0] * (i + 1) for i in range(limit)]
    for i in range(len(ways)):
        ways[i][-1] = 1
        if (pn := sum(ways[i])) % divisor == 0:
            return i + 1
        print(pn)

        try:
            ways[i + 1][0] += pn
        except:
            pass

        for k in range(1, i + 1):
            try:
                ways[i + k + 1][k] += sum(ways[i][k:])
            except:
                break
    return "not found"

print(p(10000, 100000)) # 'not found' 