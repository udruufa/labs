pass_1 = str(input())
pass_2 = str(input())
if pass_1 == pass_2:
    if len(pass_1) >= 8:
        print("Пароль принят")
    else:
        print("Должно быть >= 8 символов")
else:
    print("Пароль не принят")
