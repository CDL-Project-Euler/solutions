import copy


def coin_sums(total: int) -> int:
    """Return all ways to combine british coins to get to total pence."""
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


# def coin_sums_2(sum_to: int, coins: list) -> int:
#     """Assumes coins is descending and does not contain 0."""
#     perms = {0: 1}

#     for coin in coins:
#         temp = copy.copy(perms)
#         for val in perms:
#             for new_val in range(val + coin, sum_to+1, coin):
#                 if new_val in perms:
#                     temp[new_val] += perms[val]
#                 else:
#                     temp[new_val] = perms[val]
#         perms = temp
#         print(perms)

#     if sum_to in perms:
#         return perms[sum_to]
#     else:
#         return 0


if __name__ == "__main__":
    print(coin_sums(200))
    # print(coin_sums_2(200, [200, 100, 50, 20, 10, 5, 2, 1]))
