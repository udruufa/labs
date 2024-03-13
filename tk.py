def bilet():
    sum_1 = 0
    sum_2 = 0
    biletic = input("Введите номер билета ")
    if len(biletic) % 2 == 1:
        print("Тут нечетно(")
        bilet()
    else:
        l = len(biletic) // 2
        l1 = biletic[:l]
        l2 = biletic[l:]
        for i in l1:
            sum_1 += int(i)
        for j in l2:
            sum_2 += int(j)
        print(sum_1, sum_2)
        if sum_1 == sum_2:
            print("Билетик счастливый)")
        else:
            print("Иди еще купи билетик")
bilet()
