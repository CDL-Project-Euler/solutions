# it will either (i) become a palindrome in less than fifty iterations, 
# or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
def is_palindrome(n: int):
    if str(n) == str(n)[::-1]:
        return True
    return False

def is_lychrel(num: int):
    #iterates 50 times max
    for _ in range(50):
        num += int(str(num)[::-1])
        if is_palindrome(num):
            return False
    return True

def lychrel_count(maximum: int):
    #The number of lychrel numbers below maximum
    count = 0
    for number in range(1, maximum):
        if is_lychrel(number):
            count += 1
    return count

if __name__ == "__main__":
    print(lychrel_count(10000))
