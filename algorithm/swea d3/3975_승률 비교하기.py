# TC = int(input())
# result = ''
# for i in range(1, TC + 1):
#     A, B, C, D = map(int, input().split())
#     if A / B > C /D:
#         res = 'ALICE'
#     elif A / B == C/ D:
#         res = 'DRAW'
#     else:
#         res = 'BOB'
#     result += '#'+str(i)+ ' ' + res + '\n'
#
# print(result)






TC = int(input())
for i in range(1, TC + 1):
    A, B, C, D = map(int, input().split())
    if A / B > C /D:
        res = 'ALICE'
    elif A / B == C/ D:
        res = 'DRAW'
    else:
        res = 'BOB'
    print(f'#{i} {res}')