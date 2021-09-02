import sys

sys.stdin = open('input.txt', 'r')
TC = int(input())
for tc in range(1, TC + 1):
    text = input()
    H = int(input())
    hypn = list(map(int, input().split()))
    dict = {}
    res = ''
    for h in range(len(text) + 1):   # 2 3 2 이면 dict= {0:0 , 1 :0, 2:2 : 3:1 ......}
        dict[h] = hypn.count(h)
    for i in range(len(text)):
        res +=  '-' * dict[i] + text[i]
    res = res + '-' * dict[len(text)]
    print(f'#{tc} {res}')
