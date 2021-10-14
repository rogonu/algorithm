a = [False, False] + [True] * 1000
lst = []
for i in range(2, 1000):
    if a[i]:
        lst.append(i)
        for j in range(2*i, 1000, i):
            a[j] = False

print(lst)