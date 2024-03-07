def z_1():
    a = int(input())
    if a % 3 == 0:
        print("delit")
    else:
        print("nedelit")


def z_2():
    try:
        a = int(input())
        b = 100
        c = b / a
        print(c)
    except (ValueError, ZeroDivisionError):
        print("error")

