# alphabet = {'A': '3', 'B': '2', 'C': '1', 'D': '2', 'E': '3', 'F': '3', 'G': '2', 'H': '3', 'I': '3', 'J': '2', 'K': '2',
#             'L': '1', 'M': '2', 'N': '2', 'O': '1', 'P': '2', 'Q': '2', 'R': '2', 'S': '1', 'T': '2', 'U': '1', 'V': '1',
#             'W': '1', 'X': '2','Y': '2', 'Z': '1'}
# my_name = input()
# her_name = input()
# goonghab = ''
# for alpha in range(len(my_name)):
#     goonghab += alphabet[my_name[alpha]]
#     goonghab += alphabet[her_name[alpha]]
# while len(goonghab) > 2:
#     new_goohab = ''
#     for i in range(len(goonghab)-1):
#         new_goohab += str((int(goonghab[i]) + int(goonghab[i+1]))%10)
#     goonghab = new_goohab
# print(goonghab)

alphabet = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2, 'H': 3, 'I': 3, 'J': 2, 'K': 2,
            'L': 1, 'M': 2, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1,
            'W': 1, 'X': 2,'Y': 2, 'Z': 1}
my_name = input()
her_name = input()
goonghab = []
for alpha in range(len(my_name)):
    goonghab.append(alphabet[my_name[alpha]])
    goonghab.append(alphabet[her_name[alpha]])

while len(goonghab) > 2:
    new_goohab = []
    for i in range(len(goonghab)-1):
        new_goohab.append((goonghab[i]+goonghab[i+1])%10)
    goonghab = new_goohab
result = str(goonghab[0]) + str(goonghab[1])
print(result)
