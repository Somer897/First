import math
x = [3, 6, 9, 11, 17, 29, 33, 52, 69]
jump = int(math.sqrt(len(x)))                     # jump = len(x) ** 0.5
iskomoe = 4
index = 0
is_found = False

for i in range(0, len(x), jump):           #сам прыжок
    if iskomoe < x[i]:
        for j in range (i - jump, i):
            if x[j] == iskomoe:
                index = j
                is_found = True
                break

    if [index] == iskomoe:                     #для начального элемента и выхода из второго цикла при находе иного элемента
        break

for j in range (i, len(x)):                      #оставшийся кусок вне jump
    if x[j] == iskomoe: 
        index = j
        is_found = True
        break

if is_found:                               #нахождение элемента в списке
    print(index)
else:
    print('Not found')