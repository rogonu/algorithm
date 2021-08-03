# T = int(input('T'))
N, M = map(int, input('N M').split())

A = list(map(int, input('A').split()))
B = list(map(int, input('B').split()))

total_2=[]
if M > N:
    for i in range(M-N+1):
        total = []
        for j in range(N):  
            total.append(A[j]*B[i+j])
        total_2.append(sum(total))
    print(max(total_2))

else:
    for i in range(N-M+1):
        
        total = []
        for j in range(M):
            total.append(B[j]*A[i+j])
        total_2.append(sum(total))
    print(max(total_2))