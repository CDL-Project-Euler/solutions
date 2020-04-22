def is_pentagonal(pentagonal: int):
    """any pn in the pentagonal sequence is p = ½n(3n-1):
    Solving with quadratic formula reveals n is only an integer if (1+24p) ** 0.5 is an integer and == 5 modulo 6"""
    if pentagonal == 0:
        return False
    
    if int((1+24*pentagonal)**0.5) == (1+24*pentagonal)**0.5 and ((1+24*pentagonal)**0.5)%6 == 5:
        return True
    return False

def inle_44():
    minimum = 0
    for n1 in range(1, 10000):
        for n2 in range(n1 + 1, 10000):
            pent1 = 0.5*n1*(3*n1-1)
            pent2 = 0.5*n2*(3*n2-1)
            if is_pentagonal(pent1 + pent2) and is_pentagonal(pent2-pent1):
                print(pent1,pent2)
                minimum = min(minimum, pent2-pent1)
    return minimum

if __name__ == "__main__":
    print(inle_44())
