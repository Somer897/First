f = open('text.txt', 'r', encoding='UTF-8').read()
text = f.split()
words = {}

for item in text:
    if item in words:
        words[item] += 1
    else:
        words.update({item:1})

print(words)