#Uses the fact that the total paths to a vertice resembles pascals triangel => I use combinations
def lattice_paths(num: int):
    paths = 1
    for x in range(num):
        paths *= (2*num-x)/(num -x)
    return(paths)

if __name__ == "__main__":
    print(lattice_paths(20))