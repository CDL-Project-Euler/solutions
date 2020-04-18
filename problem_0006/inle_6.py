def sumofsquares(n):
    '''Returns the sum of the squares of the first n natural numbers'''
    return n*(n+1)*(2*n+1)/6

def squareofsum(n):
    '''Returns the square of the sums of the first n natural numbers'''
    return (n*(n+1)/2)**2

def problem6():
    print(squareofsum(100) - sumofsquares(100))

if __name__ == "__main__":
    problem6()