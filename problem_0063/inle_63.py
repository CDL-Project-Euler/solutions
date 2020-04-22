def problem_63():
    count = 1
    for integer in range(1,10):
        n = 1
        while integer > (10**(n-1)) ** (1/n):
            if len(str(integer ** n)) == n:
                count += 1
                print(integer, " : ", integer ** n)
            n += 1
    return count

if __name__ == "__main__":
    print(problem_63())