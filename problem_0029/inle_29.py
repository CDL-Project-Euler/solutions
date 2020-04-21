def problem29():
    power_list =[]
    for a in range(2, 100+1):
        for b in range(2, 100+1):
            power = a**b
            if not power in power_list:
                power_list.append(power)
    return len(power_list)

if __name__ == "__main__":
    print(problem29())