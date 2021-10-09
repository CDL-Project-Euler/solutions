from itertools import combinations, permutations


class Solution:
    def __init__(self, size: int, max_search: int):
        self.size = size
        self.max_search = max_search
        self.initialize_primes()
    
    def solve(self) -> None:
        concat_sets = self.prime_concat_sets(self.size)
        if not concat_sets:
            print("No solution found!")
        else:
            min_sum = sum(concat_sets[0])
            min_i = 0
            for i in range(1, len(concat_sets)):
                if sum(concat_sets[i]) < min_sum:
                    min_sum = sum(concat_sets[i])
                    min_i = i
            smallest = concat_sets[min_i]
            print("Smallest set with size", self.size, "has sum", min_sum, "and elements", smallest)

    def checkprime(self, value: int) -> bool:
        '''Returns whether value is prime.'''
        if value < self.max_search:
            return self.are_primes[value]
        factor = 2
        sqrt = value ** 0.5
        while factor <= sqrt:
            if value % factor == 0:
                return False
            factor += 1
        return True

    def initialize_primes(self) -> None:
        '''Initialize self.are_primes storing boolean values for primes and self.primes list.'''
        self.primes = list()
        self.are_primes = [True] * self.max_search
        self.are_primes[0] = self.are_primes[1] = False

        for (i, is_prime) in enumerate(self.are_primes):
            if is_prime:
                self.primes.append(i)
                for n in range(i*i, self.max_search, i):
                    self.are_primes[n] = False
    
    def is_concat_with_set(self, to_check: int, prime_set: list) -> bool:
        '''
            Returns whether the first value in prime_set can be 
            concatenated with all other values to produce primes.
        '''
        for prime in prime_set:
            if not(to_check in self.concat_dict[prime] and prime in self.concat_dict[to_check]):
                return False
        return True

    def prime_concat_sets(self, size: int) -> list[list]:
        '''Return all possible prime-concatenable sets of primes'''
        if size == 1:
            return [[prime] for prime in self.primes]
        if size == 2:
            concat_sets = []
            for prime2 in self.primes:
                for prime1 in self.primes: # Loop through all primes or Loop through all primes in 
                    if prime1 >= prime2:
                        break
                    if self.checkprime(int(str(prime1) + str(prime2))) and self.checkprime(int(str(prime2) + str(prime1))):
                        concat_sets.append([prime1, prime2])
            return concat_sets

        # Stores all possible sets of primes of size size that concatenate to only primes
        concat_sets = []
        smaller_sets = self.prime_concat_sets(size-1)
        self.set_concat_dict(smaller_sets)
        print("searching size:", size)
        print("Matching with", len(smaller_sets), "sets of size", size - 1)
        for smaller_set in smaller_sets:
            for prime in self.concat_dict[smaller_set[-1]]: # Loop through all primes which match
                if prime <= smaller_set[-1]:
                    break
                if self.is_concat_with_set(prime, smaller_set):
                    concat_sets.append(smaller_set + [prime])
        return concat_sets
    
    def set_concat_dict(self, concat_sets: list[list]) -> None:
        '''Initializes self.concat_dict for which each value is a list of concatenable primes with that key.'''
        concat_dict = dict()
        for concat_set in concat_sets:
            for val in concat_set:
                if val not in concat_dict:
                    concat_dict[val] = list()
                for val2 in concat_set:
                    if val2 != val:
                        concat_dict[val].append(val2)
        new_concat_dict = dict()
        for key in concat_dict:
            new_concat_dict[key] = sorted(list(set(concat_dict[key])), reverse=True)
        self.concat_dict = new_concat_dict
                    

if __name__ == "__main__":
    solution = Solution(5, 10000)
    solution.solve()
    