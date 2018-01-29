import pickle

name = '2016.db'
field = 'Фамилия'
math = 'Математика'
phys = 'Физика'
value = 'ов'


with open(name, "rb") as f:
    data = pickle.load(f)
    for key, item in data.items():
        print(field, ':\t',  item[field], '\t', math, ':\t', item[math],
              '\t', phys, ':\t', item[phys])

print()
print('-------------------')
print()
for key, item in data.items():
    if value in item[str(field)]:
        print(field, ':\t', item[field], '\t', math, ':\t', item[math],
              '\t', phys, ':\t', item[phys])