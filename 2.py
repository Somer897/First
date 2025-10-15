import numpy as np
import pandas as pd
import random
r = {}
for i in range(1, 3):
    name = input('Имя: ')
    sname = input('Фамилия: ')
    pname = input('Отчество: ')
    date = input('Дата рождения:')
    id = (random.randint(1000, 9999))
    n = {'Имя': name,
        'Фамилия': sname,
        'Отчество': pname,
        'Дата рождения': date}
    r.update({id:n})

df = pd.DataFrame(r.values(), index=r.keys())
print(df)              #DataFrame
df.to_csv('D:/1.csv')        #Save in disk D: as escel
df.to_csv('D:/1.csv', encoding='Unicode-1231')        #