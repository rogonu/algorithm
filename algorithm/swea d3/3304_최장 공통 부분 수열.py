TC = int(input())
for tc in range(1, TC + 1):
    a, b = input().split()
    pos_a = pos_b = 0
    res = 0
    while pos_a < len(a) and pos_b < len(b):
        for i in range(pos_b, len(b)):
            if a[pos_a] == b[i]:
                res += 1
                pos_b = i+1
                break
        pos_a += 1

    print(f'#{tc} {res}')
''' pos_a =     pos_b  = 
    a c a y k p
    c a p c a k
    
    d a k k k k k k k k k k k k k k k k k k k k
    d k k k k k k k k k k k k k k  k k k a
    
'''