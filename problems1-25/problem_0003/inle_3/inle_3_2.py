def largest_prime_factor(num, prev_max = 2):
    for pos_fact in range(prev_max, num):
        if num % pos_fact == 0:
            return largest_prime_factor(int(num / pos_fact), pos_fact)
    return num

print(largest_prime_factor(600851475143))