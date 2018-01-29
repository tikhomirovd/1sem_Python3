# Создать меню, состоящее из пунктов:
# 1) создать файл, в котором будут сохраняться записи (3-4 поля, использовать словари)
# 2) добавить в файл новую запись
# 3) вывести информацию из файла
# 4) поиск по 1 или 2 полям, поиск по ранжу чисел
# 5) удаление по фильтру
import os
import pickle
from pathlib import Path

DB_PATH = os.getcwd()
print(DB_PATH)
FIELD_LOGIN = "Фамилия"
FIELD_SESSION = "Сдано"
FIELD_BAN = "Шанс"
FIELDS = [FIELD_LOGIN, FIELD_SESSION, FIELD_BAN]
name = ""


def display_menu():
    print('Выберите интересующий вас пункт меню:\n')
    print('1) Добавить новую запись в базу данных')
    print('2) Выбор тех у кого сдано от a до b включительно ')
    print('3) Вывести информацию из базы данных')



def update_file(name):
    print(name)
    while True:
        field_login = input('Введите фамилию ')
        if not field_login.isdigit():
            break
        print('Введите правильно фамилию ')
    while True:
        field_session = input('Сколько сдано  ')
        if field_session.isdigit() and 0 <= int(field_session) <= 100:
            break
        print('Введите ')
    while True:
        field_ban = input('Шанс ')
        if field_ban.isdigit() and 0 <= int(field_ban) <= 100:
            break
        print('Введите балл от одного до 100 ')


    with open(name, "rb+") as f:

        data = pickle.load(f)

        data[str(len(data))] = {
            FIELD_LOGIN: field_login,
            FIELD_SESSION: field_session,
            FIELD_BAN: field_ban
        }

    with open(name, "wb+") as f:
        pickle.dump(data, f)


def print_file(name):
    print(name)
    with open(name, "rb") as f:
        data = pickle.load(f)

    for key, item in data.items():
        print(key, end=' ')
        print(item)




def searchballs():
    name = "Laba.db"
    print(name)
    f = open(name, "rb")
    data = pickle.load(f)
    c = []
    a = int(input('Введите нижнюю границу'))
    b = int(input('Введите верхнюю границу'))
    if a > b:
        print('Нижняя граница должна быть меньше верхней ')
    else:
        for key, item in data.items():
            if a <= int(item['Сдано']) <= b:
                c.append(item)
        if len(c) == 0:
            print('Таких людей нет')
        else:

            for i in range (len(c)):
                print(c[i])



def wait_for_choice():
    name = "Laba.db"
    choices = ["1", "2", "3"]
    choice = input()

    if choice == "1":
        update_file(name)
    elif choice == "3":
        print_file(name)
    elif choice == "2":
        print_file(name)
        searchballs()



    print()
    display_menu()
    wait_for_choice()


display_menu()
wait_for_choice()
