s = 0 
f1 = 1
f2 = 2

f_old = f1
f_new = f1

while f_new < 4000000:
    if f_new % 2 == 0:
        s += f_new
    f_new_temp = f_new
    f_new = f_new_temp + f_old
    f_old = f_new_temp

print(s)