# c = (a**2 + b**2)**0.5 by definition
#so 1000 = a + b + (a**2 + b**2)**0.5
# So a and b must be <= (1000)

def triplet_product(num: int):
    '''returns a pythagorean triplet'''
    for a in range(1,num):
        for b in range(1,num):
            if ((a**2 + b**2)**0.5)%1 == 0 and num == a + b + (a**2 + b**2)**0.5:
                return(a * b * (a**2 + b**2)**0.5)

if __name__ == "__main__":
    print("a * b * c = ", int(triplet_product(1000)))