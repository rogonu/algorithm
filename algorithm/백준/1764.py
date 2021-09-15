import sys
sys.stdin = open('input.txt')
N, M = map(int, input().split())
dutdo = []
bodo =[]
dutbodo = []
def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return target # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None
for _ in range(N):
    dutdo.append(sys.stdin.readline().strip())
# for _ in range(M):
#     bodo.append(sys.stdin.readline().strip().split())
for i in range(M):
    a = sys.stdin.readline().strip()
    if binary_search(a, dutdo):
        dutbodo.append(a)
dutbodo.sort()



# for _ in range(M):
#     bodo.append(input())
# dutdo = set(dutdo)
# bodo = set(bodo)
# dutbodo = dutdo & bodo
# dutbodo = list(dutbodo)
# dutbodo.sort()
print(len(dutbodo))
for j in range(len(dutbodo)):
    print(dutbodo[j])