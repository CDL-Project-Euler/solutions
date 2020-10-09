def converge_to_frac(converge: list):
    '''Converts a list of the convergents of a number to a fraction
    returns numerator and denomenator of fraction
    '''
    n = 1
    d = converge[-1]
    for c in converge[-2::-1]:
        n, d = d, c*d + n
    n,d = d,n
    return n,d

def e_converge(n:int):
    '''generates the first n convergents of e'''
    converge = [2,1,2]
    k = 2
    while len(converge) < n:
        converge += [1,1, 2*k]
        k+=1
    return converge[:n] #only returns first n terms

if __name__ == "__main__":
    n, d = converge_to_frac(e_converge(10))
    print(n,"/",d)
    print(sum([int(dig) for dig in str(n)])) # sums digits