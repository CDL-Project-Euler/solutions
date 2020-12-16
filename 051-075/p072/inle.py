def problem_72(limit: int) -> int:
    arr = [i for i in range(2, limit + 1)] # Stores totient of integers from 2 - i inclusive

    for i in range(2, limit + 1): # Index is i - 2
        if arr[i - 2] == i: # If prime, multiplies by 1 - 1/prime
            for m in range(i - 2, len(arr), i):
                arr[m] = arr[m] - arr[m] // i # Integer division speeds up

    return sum(arr)

if __name__ == "__main__":
    print(problem_72(1000000))