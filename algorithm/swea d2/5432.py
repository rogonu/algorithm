import sys
sys.stdin = open('input.txt', 'r')

def check():
    cnt = 0
    result = 0
    for i in range(len(bar)):
        if bar[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if bar[i-1] == '(':
                result += cnt
            else :
                result += 1


    return result

TC = int(input())
for tc in range(1, TC +1):
    bar = input()
    print(f'#{tc} {check()}')
