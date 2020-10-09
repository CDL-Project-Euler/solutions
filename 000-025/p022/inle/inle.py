def get_list(file_name: str):
    with open(file_name) as f:
        array = [x for x in f.read()[1:-1].split('","')]
    return(array)

def index_x_letter_sum(name_list: list):
    total = 0
    name_list.sort()
    for index in range(0, len(name_list)):
        total += sum(map(lambda x: ord(x) - 64, name_list[index])) * (index+1)
    return total

if __name__ == "__main__":
    print(index_x_letter_sum(get_list("p022_names.txt")))

