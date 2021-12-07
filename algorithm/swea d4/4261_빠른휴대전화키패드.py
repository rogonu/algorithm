TC = int(input())
for tc in range(1, TC + 1):
    S, N = input().split()
    key = {0:[],1:[], 2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],
           8:['t','u','v'],9:['w','x','y','z']}
    words = list(input().split())
    cnt = 0
    for word in words:
        temp_cnt = 0
        for i in range(len(word)):
            if word[i] in key[int(S[i])]:
                temp_cnt += 1
                if temp_cnt == len(S):
                    cnt += 1
            else:
                break
    print(f'#{tc} {cnt}')

