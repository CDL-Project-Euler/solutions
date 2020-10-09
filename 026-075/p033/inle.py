def dig_cancel_fractions():
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                if not (a == b and b==c):
                    if (10*a+b)/(10*b+c) == a/c:
                        print("case 1:",a,b,c)
                    if (10*a+b)/(10*c+b) == a/c and a!=c:
                        print("case 2:", a,b,c)
                    if (10*b+a)/(10*c+b) == a/c:
                        print("case 3:", a,b,c)
                    if (10*a+b)/(10*c+b) == a/c and a != c:
                        print("case 4:", a,b,c)

                

if __name__ == "__main__":
    dig_cancel_fractions()
    #I worked from there
