def self_powers(final:int):
    sum_pows = 0
    for integer in range(1, final + 1):
        power = 1
        for _ in range(integer):
            power = (power * integer) % (10**11)
        sum_pows += power
    return sum_pows % (10 ** 10)

if __name__ == "__main__":
    print(self_powers(1000))