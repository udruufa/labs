mesto = int(input())

if mesto in range(1, 55):
    if mesto >= 1 and mesto <= 36:
        if mesto % 2 == 0:
            print("Верхнее купе")
        else:
            print("Нижнее купе")
    else:
        if mesto % 2 == 0:
            print("Верхняя боковушка")
        else:
            print("Нижняя боковушка")
else:
    print("Вы никуда не поедете(")