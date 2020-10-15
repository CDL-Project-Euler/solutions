n = []
k = 1

def f(x):
    return k**2

while f(k) < 10000:
    if f(k) >= 1000:
        n.append(f(k))
    k += 1

print(n)
print(len(n))
print(8128%100 == 2822//100)