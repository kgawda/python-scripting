a = 1234
print("reszta z dzielenia", a % 3)
# dzielenie "zwykłe" a / 3
# dzielenie całkowite a // 3
print("bool z reszty z dzielenia", bool(a % 3))
if not (a % 3):
    print(a, "jest poniedzielna przez 3")
else:
    print(a, "nie jest poniedzielna przez 3")

a = 5 * 7
if not (a % 3):
    print("podzielna przez 3")
else:
    if not (a % 5):
        print("podzielna przez 5")
    else:
        if not (a % 7):
            print("podzielna przez 7")

if not (a % 3):
    print("podzielna przez 3")
elif not (a % 5):
    print("podzielna przez 5")
elif not (a % 7):
    print("podzielna przez 7")