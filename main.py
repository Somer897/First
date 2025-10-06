import math
import statistics
a = input().split()
for i in range(0, len(a)):
    a[i] = int(a[i])
choice = int(input('Выберите операцию: '))
match choice:
    case 0:
        minimal = min(a)
        mincol = a.count(minimal)
        if mincol >= 1:
            print(mincol)
        else:
            print(minimal)
    case 1:
        maximum = max(a)
        print(maximum)
    case 2:
        minimal = min(a)
        maximum = max(a)
        stop = maximum - minimal
        progress = list(range(minimal, minimal + maximum * stop , maximum))
        print(progress)
    case 3:
        minimal = min(a)
        maximum = max(a)
        stop = maximum - minimal
        for i in range(0, stop):
            print(minimal)
            minimal *= maximum
    case _:
        middle = int(sum(a) / len(a))
        print(middle)
        if middle < 0:
            print(0)
        else:
            middle = math.factorial(middle)
            print(middle)
