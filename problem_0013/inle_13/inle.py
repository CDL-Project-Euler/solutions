def problem13():
    sum = 0
    with open("13_input.txt", "r") as f:
        lines = f.readlines()
        for num in lines:
            sum += int(num)
    print(first_digits(sum, 10))

def first_digits(number:int, digits: int):
    '''returns the first x digits of a number'''
    power = 10 ** digits
    while number > power:
        number //= 10
    return number

if __name__ == "__main__":
    problem13()