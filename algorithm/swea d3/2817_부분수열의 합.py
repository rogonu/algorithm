def dfs(index, sumv):
    global cnt
    if index == N:
        return
    if sumv + A[index] == K:
        cnt +=1
        return
        
    dfs(index+1, sumv)
    dfs(index+1, sumv + A[index])


TC = int(input())
for tc in range(1, TC + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    dfs(0,0)
    print(f'#{tc} {cnt}')