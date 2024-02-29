import random
n = [int(i) for i in range(1, 11)]
ver = 0
never = 0
while never < 3:
    a1 = random.choice(n)
    a2 = random.choice(n)
    print(a1, "+", a2, "= ")
    a = input()
    if a1 + a2 == a and a.isnumeric():
        print("Правильно!")
        ver += 1
    else:
        print("Ответ неверный")
        never += 1
print("Игра окончена. Правильных ответов:", ver)

