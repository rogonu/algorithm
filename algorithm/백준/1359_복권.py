N, M, K = map(int, input().split())
def my_pick(pick):
    if len(pick) == M:
        add_pick = pick[:]
        pick_1.append(add_pick)

    else:
        for i in range(1,N+1):
            if i not in finish:
                if i not in pick:
                    pick.append(i)
                    my_pick(pick)
                    pick.pop()
        finish.append(i)
finish=[]
pick_1=[]
my_pick([])
print(pick_1)