def get_list(file_name: str):
    with open(file_name) as f:
        array = [x for x in f.read()[1:-1].split('","')]
    return(array)

def is_triangle(triangle: int):
    """any tn in triangle sequence is t = ½n(n+1):
    Solving with quadratic formula reveals n is only an integer if (1+8t) ** 0.5 is an integer and odd"""
    if int((1+8*triangle)**0.5) == (1+8*triangle)**0.5 and ((1+8*triangle)**0.5)%2 == 1:
        return True
    return False

def count_triangles(possible_triangles: list):
    count = 0
    for number in possible_triangles:
        if is_triangle(number):
            count += 1
    return count

def letter_sum(name_list: list):
    #Converts a list of words to a list of the sums of their numbers
    for index in range(len(name_list)):
        name_list[index] = sum(map(lambda x: ord(x) - 64, name_list[index]))
    return name_list


if __name__ == "__main__":
    print("There are", count_triangles(letter_sum(get_list("42_words.txt"))), "encoded triangles.")