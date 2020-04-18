def sundays_count():
    #months jan = 0 dec = 11
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    month = 0
    year = 1901
    # 0 is sunday, 1 is monday , jan 1 1901 was a tuesday
    day = 2
    count = 0

    while(year <= 2000):
        if day == 0:
            count += 1

        if month == 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day = (day + 29) % 7
        else:
            day = (day + month_days[month])%7

        month = (month + 1)%12

        if month == 0:
            year += 1

    return count

if __name__ == "__main__":
    print(sundays_count())

