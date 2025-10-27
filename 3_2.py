x = list(range(0, 10_000_000))
isk = 9_247_236
is_found = False
index = 0
jump = 1
for i in range(0, len(x), jump):   
    print(f"{jump}")
    jump *= 2       
    if isk < x[i]:
        start = i - jump
        end = i
        while is_found is False:
            mid = (end - (start)) // 2
            if x[mid] == isk:
                index = mid
                is_found = True
            elif x[mid] < isk:
                end = mid
            else:
                start = mid
        if is_found:
            break

        """for j in range (i - jump, i):
            if x[j] == isk:
                index = j
                is_found = True
                break"""

start = i - jump
end = i
while is_found is False:
    mid = (end - (start)) // 2
    if x[mid] == isk:
        index = mid
        is_found = True
    elif x[mid] < isk:
        end = mid
    else:
        start = mid

if is_found:                          
    print(index)
else:
    print('Not found')