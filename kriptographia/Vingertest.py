n = 33
a = [[0] * n for i in range (n)]
for i in range(n):
    a[0][i] = chr(ord('а')+i)
a[0].insert(6, chr(ord('ё')))
for i in range(1,n):
    for j in range(n):
        if j == n-1:
            t = a[i-1][0]
        else:
            t = a[i-1][j+1]
        a[i][j] = t
for i in range(n):
    print(a[i])

# ввод строки и ключа
s = str(input('Введите строку: '))
key = str(input('Введите ключ: '))

skey = key*(len(s) // len(key)) + key[:(len(s) % len(key))]
print(skey[0])



