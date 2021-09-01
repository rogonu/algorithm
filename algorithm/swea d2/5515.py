import sys
sys.stdin = open('input.txt', 'r')
TC = int(input())
for tc in range(1, TC +1):
    m, d = map(int,input().split())
    month = 1
    cnt = 0
    while month < m:

        if month in {1, 3, 5, 7, 8, 10}:
            cnt += 31
        elif month in {4, 6, 9, 11}:
            cnt += 30
        elif month == 2:
            cnt += 29
        month += 1
    cnt = cnt + d -1
    res = cnt % 7
    day = [4, 5, 6, 0, 1, 2, 3]
    print(f'#{tc} {day[res]}')