from bidict import bidict

dict_sin = bidict({})
with open('f') as f:
    for line in f:
        (s_1, s_2) = line.split()
        dict_sin[s_1] = s_2

a = str(input())
if a in dict_sin.inverse:
    print(dict_sin.inverse[a])
elif a in dict_sin:
    print(dict_sin[a])
else:
    print("Такого слова не существует")
