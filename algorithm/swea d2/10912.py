import sys
sys.stdin = open('input.txt', 'r')
TC = int(input())
for tc in range(1, TC + 1):
    text = input()
    dict = {}
    res = ''
    for i in range(97,123):  # dict에 a : 0 b :0 c:0  이렇게 만들기
        dict[chr(i)] = 0
    for j in text:
        dict[j] += 1
    for k in dict.keys():
        if dict[k] % 2:
            res += k
    if res == '':
        res = 'Good'
    print(f'#{tc} {res}')