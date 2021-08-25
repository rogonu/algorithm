A = 100
max_cnt = 0
for B in range(1, A) :
    cnt = 2
    A = 100
    while A - B > 0:
        A ,B = B, A-B
        cnt += 1
    print(cnt)