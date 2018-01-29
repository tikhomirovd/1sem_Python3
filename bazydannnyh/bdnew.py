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


def construct_db_path(name):
    return DB_PATH + '\\' + name + '.db'


def check_valid_field(field):
    if field not in FIELDS:
        print('Несуществующее поле.')
        return False
    return True


def check_valid_file(path):
    if not Path(path).is_file():
        print('Файл не существует.')
        return False
    return True


def try_input(prompt, cast):
    while True:
        try:
            return cast(input(prompt))
        except ValueError:
            pass

        print(f'Ошибка: требуется значение типа {type(cast)}.')


def display_menu():
    print('Выберите интересующий вас пункт меню:\n')
    print('1) Создать новую базу данных')
    print('2) Открыть базу данных ')
    print('3) Добавить новую запись в базу данных')
    print('4) Вывести информацию из базы данных')
    print('5) Поиск по базе данных по фамилии')
    print('6) Удаление из базы данных по фильтру')
    print('7) Выбор тех у кого баллов от a до b включительно')


def is_empty(file):
    return os.stat(file).st_size == 0


def create_file(name):
    print(name)
    open(name, "w+").close()

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
        if is_empty(name):
            data = {}
        else:
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
        if is_empty(name):
            print()
            return
        data = pickle.load(f)

        for key, item in data.items():
            print(key, end=' ')
            print(item)


def search(name, field, value):
    print(name)
    with open(name, "rb") as f:
        if is_empty(name):
            print('Поле не найдено.')
        else:
            data = pickle.load(f)
            for key, item in data.items():
                if value in item[str(field)]:
                    print(key, item)

def delete(name, field, value):
    print(name)
    f = open(name, "rb")
    if is_empty(name):
        print('Поле не найдено.')
        f.close()
    else:
        data = pickle.load(f)
        key_to_delete = None
        for key, item in data.items():
            if value in item[str(field)]:
                key_to_delete = key

        if key_to_delete is not None:
            data.pop(key_to_delete, None)
        f.close()

        with open(name, "wb+") as f:
            pickle.dump(data, f)

def filter_choise():
    print('Выберете поле: ')
    print('1) Фамилия ')
    print('2) Сдано')
    print('3) Шанс')
    field = input('Выберите поле: ')
    if field == "1":
        field = "Фамилия"
    elif field == "2":
        field = "Сдано"
    elif field == "3":
        field = "Шанс"
    return field

def name_file():
    k = os.listdir('.')
    for i in range(len(k)):
        if k[i][-2:] == 'db':
            print(k[i], end=' ,')
    global name
    name = construct_db_path(input('Введите имя базы данных: '))
    if not check_valid_file(name):
        wait_for_choice()
    return name

def searchballs():
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
    choices = ["1", "2", "3", "4", "5", "6", "7"]
    while True:
        choice = input()
        if choice in choices:
            if name != "" or choice == "1" or choice == "2":
                display_menu()
                break
            else:
                if choice in choices:
                    print('Не выбрана база данных')
                    display_menu()
        else:
            print('Несуществующий пункт меню')
            display_menu()

    if choice == "1":
        create_file(construct_db_path(input('Введите имя базы данных: ')))
    elif choice == "2":
        name_file()

    elif choice == "3":
        update_file(name)
    elif choice == "4":
        print_file(name)
    elif choice == "5":
        print_file(name)
        field = filter_choise()
        filter = input('Выберите фильтр: ')
        search(name, field, filter)
    elif choice == "6":
        print_file(name)
        field = filter_choise()
        fil = input('Выберите фильтр: ')
        delete(name, field, fil)
    elif choice == "7":
        print_file(name)
        searchballs()



    print()
    display_menu()
    wait_for_choice()


display_menu()
wait_for_choice()
