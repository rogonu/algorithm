import sys
def change(x):
    if x == 0:
        x = 1
    else:
        x = 0
    return x
sys.stdin = open('input.txt', 'r')
N = int(input())
switch = list(map(int, input().split()))
num_stu = int(input())
student = []
for _ in range(num_stu):
    student.append(list(map(int, input().split())))
for i in range(num_stu):
    if student[i][0] == 1:  # 남학생일때
        for j in range(N):
            if (j + 1) % student[i][1] == 0:
                # if switch[j] == 0:
                #     switch[j] = 1
                # else:
                #     switch[j] = 0
                switch[j] = change(switch[j])
    else:  # 여학생일때
        curp = student[i][1] - 1
        i = 1
        switch[curp] = change(switch[curp])
        # if switch[curp] == 0:
        #     switch[curp] = 1
        # else:
        #     switch[curp] = 0
        while curp - i >= 0 and curp + i < N:
            if switch[curp - i] == switch[curp + i]:
                # if switch[curp - i] == 0:
                #     switch[curp - i] = 1
                # else:
                #     switch[curp - i] = 0
                switch[curp - i] = change(switch[curp - i])
                # if switch[curp + i] == 0:
                #     switch[curp + i] = 1
                # else:
                #     switch[curp + i] = 0
                switch[curp + i] = change(switch[curp + i])
            i += 1
for w in range(N):
    print(switch[w], end=' ')
    if (w + 1) % 20 == 0:
        print()
