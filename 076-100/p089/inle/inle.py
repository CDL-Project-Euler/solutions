def get_list(file_name: str):
    with open(file_name) as f:
        array = [line.strip() for line in f]
    return(array)

def read_roman(roman: str) -> int:
    value = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    digits = list(map(lambda letter : value[letter], roman))
    number = 0
    i = 0
    while i < len(digits):
        if i < len(digits) - 1 and digits[i] < digits[i+1]:
            number += digits[i+1] - digits[i]
            i += 2
        else:
            number += digits[i]
            i += 1
    return number

def minimal_roman(n: int) -> str:
    value = [
        ["M", 1000],
        ["CM", 900],
        ["D", 500],
        ["CD", 400],
        ["C", 100],
        ["CL", 90],
        ["L", 50],
        ["XL", 40],
        ["X", 10],
        ["IX", 9],
        ["V", 5],
        ["IV", 4],
        ["I", 1]
    ]
    roman = ""
    i = 0
    while n > 0:
        if value[i][1] <= n:
            roman += value[i][0]
            n -= value[i][1]
        else:
            i += 1
    return roman


if __name__ == "__main__":
    romans = get_list('p089_roman.txt')
    total = 0
    print("orig | new | num")
    for roman in romans:
        num = read_roman(roman)
        new_roman = minimal_roman(num)w
        total += len(roman) - len(new_roman)
        print(roman, new_roman, num)
    print("Total saved:", total)
    
