import itertools as it

def arith_combos(digits:list):
    targets = []
    funcs = ["+", "-", "*", "/"]

    for func_set in it.product(funcs, repeat=3):
        for new_digs in it.permutations(digits[1:], 3):
            for parentheses in [(0, 5), (0, 9), (3, 9), (3, 12), (7,12), (0,12)]:
                equation = ["", digits[0], func_set[0],"", new_digs[0],"", func_set[1],"", new_digs[1],"", func_set[2], new_digs[2], ""]
                equation[parentheses[0]] = "("
                equation[parentheses[1]] = ")"
                try:
                    target = eval("".join(map(str, equation)))
                except ZeroDivisionError:
                    pass 
                else:
                    if target > 0 and target == target//1 and not target in targets:
                        targets.append(target)

                equation = [" ", new_digs[0], func_set[0], " ",digits[0], " ", func_set[1], " ", new_digs[1], " ", func_set[2], new_digs[2], " "]
                equation[parentheses[0]] = "("
                equation[parentheses[1]] = ")"
                try:
                    target = eval("".join(map(str, equation)))
                except ZeroDivisionError:
                    pass
                else:
                    if target > 0 and target == target//1 and not target in targets:
                        targets.append(target)
            
            if func_set[1] == "*" or func_set[1] == "/": #2 parentheses sets
                equation = ["(", new_digs[0], func_set[0], " ",digits[0], ")", func_set[1], "(", new_digs[1], " ", func_set[2], new_digs[2], ")"]
                try:
                    target = eval("".join(map(str, equation)))
                except ZeroDivisionError:
                    pass
                else:
                    if target > 0 and target == target//1 and not target in targets:
                        targets.append(target)
            
                equation = ["(", new_digs[0], func_set[0], " ",digits[0], ")", func_set[1], "(", new_digs[1], " ", func_set[2], new_digs[2], ")"]
                try:
                    target = eval("".join(map(str, equation)))
                except ZeroDivisionError:
                    pass
                else:
                    if target > 0 and target == target//1 and not target in targets:
                        targets.append(target)
    return sorted(targets)

def max_continuous(l:list):
    """Counts continuous in sorted list"""
    max_count = 1
    count = 1
    for i in range(1, len(l)):
        if l[i] == l[i-1] + 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 1
    return max_count

def max_digit_arith():
    top = 0
    for digs in it.combinations(range(1, 10), 4):
        count = max_continuous(arith_combos(digs))
        if count > top:
            max_set = digs
            top = count
            print(digs, count)
    return max_set
    
if __name__ == "__main__":
    print(max_digit_arith())