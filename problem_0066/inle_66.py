#Trying to optimize it. Didn't really work
# note y is always smaller than x, so it must be faster to look for a y which has an x, 

def diophantine_x_min(d_max: int): 
    #Find the value of D ≤ d_max in minimal solutions of x for which the largest value of x is obtained.
    x_max = 0
    d_at_x_max = 0
    for d in range(2, d_max+1):
        print('___________', d)
        if (d**0.5) != (d**0.5)//1:
            y = 1
            searching = True
            while searching:
                x = (d*(y**2)+1)**(0.5)
                if int(x)**2 == (d*(y**2)+1):
                    if x > x_max:
                        x_max = x
                        d_at_x_max = d
                        print(d, " : ", x , " : ", y)
                    searching = False
                y += 1
    return d_at_x_max

if __name__ == "__main__":
    print(diophantine_x_min(1000))