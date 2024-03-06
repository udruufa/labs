import random

g_1 = [int(i) for i in range(1, 8)]
g_2 = [int(j) for j in range(1, 8)]
sum_1 = 0
sum_2 = 0

a = random.choice(g_2)
a_i = g_2.index(a)

for i in range(7):
    sum_1 += g_1[i]
    if i == a_i:
        continue
    sum_2 += g_2[i]

if sum_1 - 4 == sum_2:
    print("4")
elif sum_1 - 4 < sum_2:
    if sum_1 - 2 == sum_2:
        print("2")
    elif sum_1 - 2 < sum_2:
        print("1")
    else:
        print("3")
else:
    if sum_1 - 6 == sum_2:
        print("6")
    elif sum_1 - 6 < sum_2:
        print("5")
    else:
        print("7")

print(sum_1, sum_2, a)
