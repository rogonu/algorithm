import sys

sys.stdin = open('input.txt', 'r')
TC = int(input())
for tc in range(1, TC + 1):
    button = list(input().split())
    button_B = []
    button_O = []
    # Blue가 움직이는 동안에 Orange도 움직여야 되므로 Blue와 Orange 의 움직임을 따로하기 위해
    # orange의 버튼위치와 blue 버튼 위치를 나눔

    for i in range(int(button[0])):
        if button[2 * i + 1] == 'B':
            button_B.append(int(button[2 * i + 2]))
        elif button[2 * i + 1] == 'O':
            button_O.append(int(button[2 * i + 2]))
    push_button = 1
    # 4 B 2 O 1 O 2 B 4
    #주어진 순서대로 버튼을 눌러야되므로 첫번째 버튼을 타겟
    pos_B = 1
    pos_O = 1
    cnt = 0


    while button_B or button_O:
        len_button = len(button_O) + len(button_B)
        if button_B:
            if pos_B < button_B[0]:
                pos_B += 1
            elif pos_B > button_B[0]:
                pos_B -= 1
            elif pos_B == button_B[0] and button[push_button] == 'B':
                button_B.pop(0)


        if button_O:
            if pos_O < button_O[0]:
                pos_O += 1
            elif pos_O > button_O[0]:
                pos_O -= 1
            elif pos_O == button_O[0] and button[push_button] == 'O':
                button_O.pop(0)

        new_len_button = len(button_O) + len(button_B)
        if len_button != new_len_button:
            push_button += 2

        cnt += 1

    print(f'#{tc} {cnt}')
