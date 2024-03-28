import random
def zad1():
    sp = []
    for i in range(5):
        sp.append(random.randint(0,5))
    print(*sp)
    a = int(input("chislo:"))
    if a in sp:
        print("est'", '\n')
    else:
        print("net", '\n')

def zad2():
    rand = []
    zn = []
    for i in range(5):
        rand.append(random.randint(0, 5))
    rand.sort()
    for i in range(1, 4):
        if rand[i] == rand[i - 1]:
            if not (rand[i] in zn):
                zn.append(rand[i])
    print(rand, zn, '\n')

def zad3():
    dni = ("pn", "vt", "sr", "cht", "pt", "sb", "vs")
    a = random.randint(1, 7)
    print(a, "vihi:", dni[-(a):], "rab:", dni[:(7-a)], '\n')

def zad4():
    sp1 = ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1", "g1"]
    sp2 = ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2", "g2"]
    sport = ()
    for i in range(5):
        sp1.remove(random.choice(sp1))
        sp2.remove(random.choice(sp2))
    sport = sp1 + sp2
    print(*sport)

zad1()
zad2()
zad3()
zad4()

