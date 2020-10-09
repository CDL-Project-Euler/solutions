def get_list(file_name: str):
    with open(file_name) as f:
        array = [line for line in f]
    return(array)

def read_roman(roman):
    values = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    new = []
    for letter in range(len(roman)):
        if letter == 0:
            new.append([values[roman[letter]], 1])
        elif values[roman[letter]] == new[-1][0]:
            new[-1][1] += 1
        else:
            new.append([values[roman[letter]], 1])
    
    
    for i in range(len(new)):
        if new()
        num += 


if __name__ == "__main__":
    romans = get_list('p089_roman.txt')
    for i in range(len(romans)):
        roman[i] = read_roman(roman[i])
    
