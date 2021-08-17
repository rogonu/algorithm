import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    tm = list(map(int, input().split()))
    hour = tm[0] + tm[2]
    minute = tm[1] + tm[3]
    if minute > 60:
        minute -= 60
        hour += 1
    if hour > 12:
        hour -= 12

    print(f'#{tc} {hour} {minute}')
