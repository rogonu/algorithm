n, m = map(int, input().split())
up = 1
down = 1
for i in range(n,n-m,-1):
    up = up * i
for j in range(m,0,-1):
    down = down * j
res = up // down
print(res)