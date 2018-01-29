#                       Тихомиров Дмитрий
text = ['Князь Андрей находился во время сражения при убитом в этом деле ',
        'австрийском генерале Шмите. Под ним была ранена лошадь, ',
        'и сам он был слегка оцарапан в руку пулей. В знак ',
        ' особой милости главнокомандующего он был послан с ',
        'известием об этой победе к австрийскому двору, находившемуся ',
        'уже не в Вене, которой угрожали французские войска, а в Брюнне.  ',
        'Мама папа бабуля.']
tr = '1'


def f1():
    s2 = sl.split()
    if len(s2) < len(sl):
        print('Неверный формат ввода')
    else:

        slc = sl.capitalize()
        reslc = resl.capitalize()
        for i in range(len(text)):
            text[i] = text[i].split()
            for j in range(len(text[i])):
                if not text[i][j].isalpha():
                    q = text[i][j][-1:]
                    text[i][j] = text[i][j][:-1]
                else:
                    q = ''
                if text[i][j] == sl:
                    text[i][j] = resl
                elif text[i][j] == slc:
                    text[i][j] = reslc
                text[i][j] += q
            text[i] = ' '.join(text[i])
            f3()


def f3():
    wi = max([len(i) for i in text])
    for i, g in enumerate(text):
        g = g.split()
        g = ' '.join(g)
        text[i] = g
        if tr == '2':
            text[i] = g.rjust(wi, ' ')
        elif tr == '3':
            sr = len(g)
            g = g.split()
            coun = len(g) - 1
            tab = (wi - sr) // coun + 1
            ost = (wi - sr) % coun
            val = g[0]
            for j in range(1, coun + 1):
                val += (' ' * (tab + int(ost >= j)) + g[j])
            text[i] = val


while 1:
    print('\n', '\n'.join(text), '\n1. Удалить заданное слово во всем тексте.',
          '2. Произвести замену одного слова на другое во всем тексте.',
          '3. Выравнивание текста.', '4. Найти предложения, в которых во всех \
словах гласные чередуются', 'с согласными.', '5. Выйти.\n', sep='\n')
n = input()
if n == '1':
    sl = input('Введите слово, которое надо удалить:\n')
    resl = ''
    f1()
elif n == '2':
    sl = input('Введите слово, которое надо заменить:\n')
    sl = sl.split()[0]
    resl = input('Введите слово, на которое надо заменить:\n')
    f1()
elif n == '3':
    while True:
        print('1. По левому краю', '2. По правому краю', '3. По ширине',
              sep='\n')
        tr = input()
        if not len(tr) - 1 and tr in '123':
            f3()
            break
        else:
            print('Выберите правильное действие')
elif n == '4':
    f4()
elif n == '5':
    break
else:
    print('Введено неправильное значение!\n')
