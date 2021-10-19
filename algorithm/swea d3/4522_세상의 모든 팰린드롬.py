TC = int(input())
for tc in range(1, TC + 1):
    word = input()
    k = 0
    check = 0
    while k < (len(word)//2):
        if word[k] == word[-k-1] or word[-k-1] == '?' or word[k] == '?':
            check += 1
        k += 1
    if check == k:
        print(f'#{tc} Exist')
    else:
        print(f'#{tc} Not exist')


