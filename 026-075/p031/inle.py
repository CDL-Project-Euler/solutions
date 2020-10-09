def coin_sums(total: int):
    #All of the ways to combine british coins to get to total pence
    count = 0
    for two_pound in range(total // 200 + 1):
        for one_pound in range((total-200*two_pound) // 100 + 1):
            for fiftyp in range((total-200*two_pound - 100*one_pound) // 50 + 1):
                for twentyp in range((total-200*two_pound - 100*one_pound - 50 * fiftyp) // 20 + 1):
                   for tenp in range((total-200*two_pound - 100*one_pound - 50 * fiftyp - 20*twentyp) // 10 + 1):
                       for fivep in range((total-200*two_pound - 100*one_pound - 50*fiftyp - 20*twentyp - 10*tenp) // 5 + 1):
                           for _ in range((total-200*two_pound - 100*one_pound - 50*fiftyp - 20*twentyp - 10*tenp - 5*fivep) // 2 + 1):
                               count += 1
    return count

if __name__ == "__main__":
    print(coin_sums(200))