import re
a = input('Введите дату')
b = re.findall('^[1-3][0-9][\.][0-9][0-9][\.][0-9][0-9][0-9][0-9]',a)

print(b)


