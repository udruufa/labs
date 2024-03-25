day, month, year = input("data:").split('.')
if int(day) * int(month) == int(year[-2:]):
    print(True)
else:
    print(False)
