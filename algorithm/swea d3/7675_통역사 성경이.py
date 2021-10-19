TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    sentence = ''
    cnt = 0
    while cnt < N:
        sentence += input()
        for i in sentence:
            if i in ['.', '?', '!']:
                cnt += 1
    check = 0                                 # 대문자가 몇개인지 확인
    check2 = 0                                # 숫자가 들어있는지 확인
    res = [0]*N                               # 문장의 개수만큼 리스트를 만들어준다
    k = 0                                     # 한문장에 이름이 몇개 있는지 res에 넣어주기 위해 작성함.

    for j in sentence:
        if ord('A') <= ord(j) <= ord('Z'):               #대문자이면 check +1
            check += 1
        elif ord('0') <= ord(j) <= ord('9'):             # 숫자가 들어가면 check2 = 1
            check2 = 1
        elif j == ' ':
            if check == 1 and check2 == 0:            # 한단어가 끝났을때 check 와 check2를 확인하여 res[k] 갑승ㄹ += 1
                res[k] += 1
            check = 0
            check2 = 0
        elif j in ['.', '?', '!']:                     # 문장이 끝났을때도 check와 check2를 확인하여 res[k] += 1 해주고 k +=1 해주어서 res[k]가 들어가 위치를 바꿔준다.
            if check == 1 and check2 == 0:
                res[k] += 1
            check = 0
            check2 = 0
            k += 1
    print(f'#{tc}', end=' ')
    print(*res)

