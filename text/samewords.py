#  Найти прелдложение с максимальным количеством слов, начинающихся на заданную букву
alphabet = '''ABCDEFGHIJKLMNOPQRSTUVWXYZ,;:
              АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЫЮЯ'''
infile = open('dems.txt', 'r')
f = infile.readline()
f1 = infile.readline()
print(f)
print(f1)
s = infile.read().upper().strip().split()
x = input('Введите букву ')
print(s)
a = len(s)
d = []
e = ['']
k = 0
j = 0
for i in range(a):
    if s[i][-1] in alphabet:
        e[j] += s[i] + ' '
        if s[i][0] == x.upper():
            k += 1
    else:
        e[j] += s[i]
        e.append('')
        j += 1
        if s[i][0] == x.upper():
            k += 1
        d.append(k)
        k = 0

maximum = max(d)
zz = d.index(max(d))

if maximum == 0:
    print('Нет слов, начинающихся на такую букву')
else:
    print(e[zz])
    print('Количество слов, начинающихся на данную букву', maximum)



