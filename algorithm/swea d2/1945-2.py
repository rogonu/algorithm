# N = 2**a * 3**b * 5**c 7**d * 11**
k = int(input())
def dlstn(n):
    a = 0 
    b = 0
    c = 0
    d = 0
    e = 0
    while n % 2 == 0:
        n = n / 2
        a += 1 
    while n % 3 == 0:
        n = n / 3
        b += 1 
    while n % 5 == 0:
        n = n / 5
        c += 1 
    while n % 7 == 0:
        n = n / 7
        d += 1 
    while n % 11 == 0:
        n = n / 11
        e += 1 


dlstn(k)


