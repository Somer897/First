#функция сортировки пузырьком
def bs(spisok):
    k = 0
    swapped = True
    while swapped:
        swapped = False
        for j in range(len(spisok)-1):
            if spisok[j]<spisok[j+1]:
                spisok[j], spisok[j+1] = spisok[j+1], spisok[j]
                swapped = True
                k += 1
    print('Список: ', spisok,'Количество оперций',  k)

#функция сортировки выборкой
def ss(spisok):
    k = 0
    for i in range(len(spisok)):
        mini  = i 
        for j in range(i + 1, len(spisok)):   
            if spisok[j] > spisok[mini]:  
                mini = j
        spisok[i], spisok[mini] = spisok[mini], spisok[i]
        k += 1
    print('Список: ', spisok,'Количество оперций',  k)

#итоговая функция, выбирает какая сортировка
def itog(ch, spisok):
    if ch == 1:
        bs(spisok)
    elif ch == 2:
        ss(spisok)
    else:
        print('error')
        

#создание списка
def lst(list):
    for i in range(0, len(list)):
        list[i] = int(list[i])

#список задан
spisok = input('Введите список').split()
#операция задана
ch = int(input('Введите операцию: '))

#преобразование списка
lst(spisok)
#вызов итоговой функции
itog(ch, spisok)