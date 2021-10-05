import sys
sys.stdin = open('input.txt', 'r')
TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    d = ''

    # for _ in range((N-1)//20+1):
    #
    #     temp = list(input().split())
    #     for i in temp:
    #         d += i
    nums = 0
    while len(d) < N:
        d += ''.join(input().split())
    while True:
        if str(nums) not in d:
            res = nums
            break
        nums += 1
    print(f'#{tc} {res}')