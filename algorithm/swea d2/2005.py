import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Arr = []
    print(f'#{tc}')
    for i in range(1,N+1):

        if i != 1 and i != 2:
            for j in range(1,i-2):
                Arr[i]= Arr[i] + Arr[i-1]
        Arr.append(1)
        print(' '.join(map(str, Arr)))