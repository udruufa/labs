
def zad1():
    a = int(input())
    if a % 3 == 0:
        print("da")
    else:
        print("net")

def zad2():
    a = input()
    try:
        c = 100 / int(a)
        print(c)
    except (ValueError, ZeroDivisionError):
        print("error")

def zad3():
    day, month, year = input("data:").split('.')
    if int(day) * int(month) == int(year[-2:]):
        print(True)
    else:
        print(False)

def zad4():
    sum_1 = 0
    sum_2 = 0
    biletic = input("Введите номер билета ")
    if len(biletic) % 2 == 1:
        print("Тут нечетно(")
        zad4()
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

zad3()
zad4()