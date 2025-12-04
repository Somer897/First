def simple(num, n):
    a = num
    if num == 1:
        n.append(num)
        return n
    else:
        for i in range(2, int(num//2)):
            if num % i == 0:
                n.append(i)
                num = num / i
                break
        if num == a:
            n.append(num)
            return n
        else:
            return simple(num, n)

num = 56
n = [1]
print(simple(num, n))