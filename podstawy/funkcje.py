def f1(a, b, c):
    return a * b + c

def powitanie(imie, stanowisko='dyr.', ilosc_wykrzyknikow=3, tytuly=None, wykrzyknik='!'):
    result = "Witaj " + stanowisko + " "
    if tytuly is not None:
        result += " ".join(map(str, tytuly))
        result += " "
    result += imie + " " + wykrzyknik * ilosc_wykrzyknikow
    return result

assert f1(1, 2, 3) == 5
assert f1(1, 2, c=3) == 5
# assert f1(a=1, b=2, 3) == 5  # pozycyjne muszą być przed kluczowymi
assert f1(a=1, b=2, c=3) == 5
assert f1(b=2, c=3, a=1) == 5  # kluczowe nie zależą od kolejności
print(powitanie("Stanisław"))
print(powitanie("Ignacy", stanowisko="majster", tytuly=["hr.", "ks.", "jm"]))
print(powitanie("Wacław", 'rektor'))
print(powitanie("Henryk", wykrzyknik='?'))

def f2():
    return 1, "Hej"

liczba, napis = f2()
print(f"Liczba {liczba}, napis {napis!r}")
tupla_liczba_napis = f2()

t1 = 1, "Hej"
t2 = (1, "Hej")
assert t1 == t2
t1 = 1,  # zapakowanie jednego elementu w tuplę
t2 = (1,)
assert t1 == t2

t1 = (1, "Hej")
x1, x2 = t1  # odpakowanie tupli dwuelementowej
# x1 = t1[0]
# x2 = t1[1]
assert x1 == 1
assert x2 == "Hej"

x1, = (1,)  # odpakowanie tupli jednoelementowej

