def char_sum(word: str) -> int:
    """Sum letter indices of uppercase word."""
    total = 0
    for letter in word:
        total += ord(letter) - 65
    return total


def length_1st(a: list) -> int:
    return len(a[0])


def anagr_sqr(a: str, b: str):
    start = (10 ** len(a)) ** 0.5
    end = (10 ** (len(a) - 1)) ** 0.5
    for i in range(len(a), ):  # Loop through nums for a is bigger
            
    # loop through nums for b is biggers
    return None


def solve():
    # Read in words
    with open("98_input.txt") as f:
        words = [word[1:-1] for word in f.readline().split(",")]
    # Build set of anagrams
    word_dict = dict()
    anagrams = dict()
    for word in words:
        if (key := str(sorted(word))) in word_dict:
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word_dict[key], word]
        else:
            word_dict[key] = word

    ana_list = []
    for key in anagrams:
        ana_list.append(anagrams[key])
    ana_list.sort(reverse=True, key=length_1st)
    
    for anagram in ana_list:
        if (maximum := anagr_sqr(anagram))
            print(maximum)
            return


if __name__ == "__main__":
    solve()