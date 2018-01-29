while True:
    print('Чтобы закончить программу введите пустую строку ')
    R = input('Введите строку ')
    if R == "":
        break
    A = input('Введите подстроку ')
    if A == "":
        break
    a = 0

    for i in range(len(A)):
        if A.count(A[i]) <= R.count(A[i]):
            a += 1
    if a == len(A):
        print('Можно составить')
    else:
        print('Нельзя составить ')