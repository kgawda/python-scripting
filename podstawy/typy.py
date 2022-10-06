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
# if not (a % 3):
#     print("podzielna przez 3")
# else:
#     if not (a % 5):
#         print("podzielna przez 5")
#     else:
#         if not (a % 7):
#             print("podzielna przez 7")

if not (a % 3):
    print("podzielna przez 3")
elif not (a % 5):
    print("podzielna przez 5")
elif not (a % 7):
    print("podzielna przez 7")

# for _ in range(5):
#     print("Hej!")

# Komentarze wielonilijkowe - tak naprawdę to stringi nie przypisane do zmiennej
"""Komentarz
wielo
lnijkowy"""
# podobnie jak:
"Jakiś string"
'Inny string'
12345
True
'''Inny string
wielolinijkowy
'''

# # po stringu można iterować
# for x in "Hej!":
#     print(x)

# Listy i indeksowanie
l = ["A", "B", "C", "D"]
assert l == list("ABCD")

assert l[0] == "A"
assert l[3] == "D"
assert l[len(l) - 1] == "D"
assert l[-1] == "D"
assert l[-2] == "C"
l[-2] = "c"
assert l[2] == "c"

# Slice
# od jakiego indeksu chemy zacząć : jakiego indeksu nie chcemy ("nawais otwarty")
assert l[1:3] == [l[1], l[2]]
assert l[1:4] == [l[1], l[2], l[3]]

assert l[1:-1] == l[1:3]
assert l[1:] == l[1:4]  # do końca
assert l[:3] == l[0:3]  # od początku
assert l[:] == l  # kopia

l[1:3] = ["b", "C"]
assert l == ["A", "b", "C", "D"]
# del l[1:3]
# print(l)

assert "Ala ma kota"[1:-1:2] == "l akt"
assert "Ala ma kota"[::3] == "A  t"
assert "Ala ma kota"[11:0:-1] == "atok am al"  # podając indeks "końcowy" nie da się dojechać wspak do początku
assert "Ala ma kota"[::-1] == "atok am alA"

l[::2] = ["A!", "C!"]
print(l)
assert l == ['A!', 'b', 'C!', 'D']
