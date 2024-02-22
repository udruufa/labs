pass_1 = input(str())
pass_2 = input(str())
if pass_1 == pass_2:
    if len(pass_1) >= 8:
        print("Пароль принят")
    else:
        print("Должно быть >= 8 символов")
else:
    print("Пароль не принят")