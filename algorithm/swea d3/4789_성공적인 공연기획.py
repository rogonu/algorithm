TC = int(input())
for tc in range(1, TC + 1):
    people = list(map(int, input()))
    noozuk = 0
    need = 0
    for i in range(len(people)):
        if noozuk >= i:
            noozuk += people[i]
        else:
            need += i-noozuk
            noozuk += people[i]+ i-noozuk
    print(f'#{tc} {need}')