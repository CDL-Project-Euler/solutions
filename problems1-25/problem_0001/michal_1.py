mult = []

for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        mult.append(i)
print(sum(mult))

