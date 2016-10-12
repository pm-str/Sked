fin = open('data.txt', 'r')

info = ''
word = ''
desc = ''

l = []

for i in fin:
    if i.startswith('###'):
        l.append((word, desc))
        word = desc = ''
    else:
        if not word:
            word = i
        else:
            desc += i
print(l[:10])