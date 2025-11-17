f = open('text.txt', 'r', encoding='UTF-8').read()
text = f.split()
words = {}

for i in text:
    for j in i:
        if j in words:
            words[j] += 1
        else:
            words.update({j:1})

print(words)