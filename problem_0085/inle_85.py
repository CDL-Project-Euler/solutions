#if a w x 1 rect has n rectangles
#and a h x 1 rect has m rectangles
# a rectangle with dimensions w by h will have n*m rectangles
# there are n + 1 - z ways a z long rect can be placed in a n x 1 rect 
# so there are  1 + 2 + ... + n = n(n+1)/2 number of possible rects in a n x 1 rectangle
def counting_rect(num_rects):
    #Although there exists no rectangular grid that contains exactly two million rectangles, 
    #find the area of the grid with the nearest solution to num_rects.
    minimum_dist = num_rects
    area_at_min = 0

    for width in range(1, num_rects):
        height = 1
        while True:
            count = (height)*(height+1)*(width)*(width + 1)/4
            if minimum_dist ** 2 > (num_rects - count) ** 2:
                minimum_dist = ((num_rects - count) ** 2) ** 0.5
                area_at_min = height * width
                x = width
                y = height
            if count > num_rects:
                break
            height += 1
    print(x, y, minimum_dist)
    return area_at_min

if __name__ == "__main__":
    print(counting_rect(2000000))
        
    
