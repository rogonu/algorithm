def change(soosik):
    st = []
    hoowi = ''
    for i in soosik:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            hoowi += i
        else:
            while st:
                hoowi += st.pop()
            st.append(i)
    while st:
        hoowi += st.pop()
    return hoowi


def calculation(hoowi):
    st_2 =[]
    res = 0
    for j in hoowi:
        if j in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            st_2.append(int(j))
        else:
            num1 = st_2.pop()
            num2 = st_2.pop()
            st_2.append(num1 + num2)
    return st_2[0]


TC = 10

for tc in range(1, TC + 1):
    n = input()
    soosik = input()
    hoowi = change(soosik)

    print(f'#{tc} {calculation(hoowi)}')
