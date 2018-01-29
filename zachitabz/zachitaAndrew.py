# Программа хранит данные в файле, выполняет с ними
# операции, прописанные в меню(работа с таблицей данных).

# Леонов Андрей

# fn - основной файл
# new - Новая бд
# sortalph - сортировка записей по алфавиту
# pr - вывод записей
# pr1 - вывод неотсортированных записей
# poisk1,poisk2 - поиски по критериям
# newzap - добавление записи
# sort - сортировка численная
# remove - удаление записи
# red - редактирование записи

import pickle

fn = 'qwert1.bin'
fn2 = 'copy.bin'
p2 = 'poisk2.bin'
s = 'sort.bin'


def new():
    k = 0
    with open(fn, 'wb') as f:
        pickle.dump(k, f)


def pr(fname):
    with open(fname, 'rb') as f:
        k = pickle.load(f)
        for i in range(k):
            a = pickle.load(f)
            print('{:2d}'.format(a['n']), '%-15s' % a['f'],
                  '{:4d}{:4d}{:4d}'.format(a['w'], a['ni'], a['l']))
        print('--------------------------------------------------------')
        print()


def newzap(fn):
    b = {}
    with open(fn, 'rb') as f:
        k = pickle.load(f)
        with open(fn2, 'wb') as p:
            for i in range(k):
                a = pickle.load(f)
                pickle.dump(a, p)
    b['n'] = k + 1
    b['f'] = ''
    b['w'] = ''
    b['ni'] = ''
    b['l'] = ''
    while not b['f'].isalpha():
        b['f'] = str(input('Введите марку сигарет: '))
    while not b['w'].isdigit():
        b['w'] = str(input('Введите содержание смол: '))
    while not b['ni'].isdigit():
        b['ni'] = str(input('Введите содержание никотина: '))
    while not b['l'].isdigit():
        b['l'] = str(input('Введите цену за пачку: '))
    b['w'] = int(b['w'])
    b['ni'] = int(b['ni'])
    b['l'] = int(b['l'])
    with open(fn, 'wb') as f:
        pickle.dump(k + 1, f)
        with open(fn2, 'rb') as p:
            for i in range(k):
                a = pickle.load(p)
                pickle.dump(a, f)
        pickle.dump(b, f)

    return (fn)


def poisk1(fn):
    value = 'а'
    count = 0
    with open(fn, 'rb') as f:
        k = pickle.load(f)
        for i in range(k):
            a = pickle.load(f)
            if value in a['f'] :
                count += 1
    with open(fn, 'rb') as f:
        k = pickle.load(f)
        with open(p2, 'wb') as p:
            pickle.dump(count, p)
            for i in range(k):
                a = pickle.load(f)
                if value in a['f']:
                    pickle.dump(a, p)


def sort(fn):
    x = []
    with open(fn, 'rb') as f:
        k = pickle.load(f)
        for i in range(k):
            a = pickle.load(f)
            x.append(a)
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if x[j]['l'] > x[j + 1]['l']:
                x[j], x[j + 1] = x[j + 1], x[j]
                x[j]['n'], x[j + 1]['n'] = x[j + 1]['n'], x[j]['n']
    with open(s, 'wb') as f:
        pickle.dump(k, f)
        for i in range(len(x)):
            pickle.dump(x[i], f)


def remove(fn):
    with open(fn, 'rb') as f:
        k = pickle.load(f)
        with open(fn2, 'wb') as p:
            for i in range(k):
                a = pickle.load(f)
                pickle.dump(a, p)
    z = 0
    while z == 0:
        v = str(input('Кого удалить? '))
        if v.isdigit():
            v = int(v)
            if v > 0 and v < k + 1:
                z += 1

    with open(fn, 'wb') as f:
        pickle.dump(k - 1, f)
        with open(fn2, 'rb') as p:
            for i in range(k):
                a = pickle.load(p)
                if a['n'] < v:
                    pickle.dump(a, f)
                if a['n'] > v:
                    a['n'] = a['n'] - 1
                    pickle.dump(a, f)


while True:
    print('Выбирете действие: ')
    print('1-Создать новую')
    print('2-Открыть существующую - просмотреть все записи')
    print('3-Добавить новую запись')
    print('4-Лёгкие(смол<10)')
    print('5-Сортировка по цене')
    print('6-Удаление записи')
    print('0-Выход')
    o = str(input())
    if o == "1":
        f = new()
        pr(fn)

    elif o == "2":
        pr(fn)

    elif o == "3":
        pr(fn)
        fn = newzap(fn)
        pr(fn)

    elif o == "4":
        pr(fn)
        poisk1(fn)
        pr(p2)

    elif o == "5":
        pr(fn)
        sort(fn)
        pr(s)

    elif o == "6":
        pr(fn)
        remove(fn)
        pr(fn)

    elif o == "0":
        break
    else:
        print('Ошибка ввода')


