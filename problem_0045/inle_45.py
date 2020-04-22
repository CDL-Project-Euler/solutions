def is_triangle(triangle: int):
    """any tn in triangle sequence is t = ½n(n+1):
    Solving with quadratic formula reveals n is only an integer if (1+8t) ** 0.5 is an integer and odd"""
    if int((1+8*triangle)**0.5) == (1+8*triangle)**0.5 and ((1+8*triangle)**0.5)%2 == 1:
        return True
    return False

def is_pentagonal(pentagonal: int):
    """any pn in the pentagonal sequence is p = ½n(3n+1):
    Solving with quadratic formula reveals n is only an integer if (1+24p) ** 0.5 is an integer and == 5 modulo 6"""
    if int((1+24*pentagonal)**0.5) == (1+24*pentagonal)**0.5 and ((1+24*pentagonal)**0.5)%6 == 5:
        return True
    return False

def is_hexagonal(hexag: int):
    """any tn in triangle sequence is t = ½n(n+1):
    Solving with quadratic formula reveals n is only an integer if (1+8t) ** 0.5 is an integer and odd"""
    if int((1+8*hexag)**0.5) == (1+8*hexag)**0.5 and ((1+8*hexag)**0.5)%4 == 3:
        return True
    return False

def problem_45(n = 1):
    """starts search at nth hexagonal number"""
    while True:
        hexagon = n*(2*n -1) 
        if is_triangle(hexagon) and is_pentagonal(hexagon):
            return hexagon
        n+=1

if __name__ == "__main__":
    print(problem_45(144))