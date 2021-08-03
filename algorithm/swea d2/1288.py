n = int(input())
k = 0
lst = []

while len(lst) != len(range(10)):
    k += 1
    a = list(map(int, str(k*n)))
    for i in a:
        if i not in lst:
            lst.append(i)
    
print(n*k)         
    
# print(n)   

# T = int(input())
# for i in range(T):
#     a = 0
#     N = int(input())
#     lst = []
#     while len(lst_)

# test_cases = int(input())

# for i in range(1, test_cases+1:
#     )