przyklady = [
    11,
    3.14,
    "test",
    ["a", "b"]
]

for x in przyklady:
    # print(x, type(x), bool(x), repr(type(x)()))
    print(f"{x} -> {bool(x)}, {type(x).__name__}() == {type(x)()!r} -> {bool(type(x)())}")

# f-string
# a = 11
# print("Zmienna a ma wartosc", a, ".")
# print("Zmienna a ma wartosc " + str(a) + ".")
# print("Zmienna a ma wartosc %s." % (a))
# print("Zmienna %s ma wartosc %s." % ('a', a))
# print("Zmienna {} ma wartosc {}.".format('a', a))
# print("Zmienna {1} ma wartosc {0}.".format('a', a))
# print("Zmienna {nazwa} ma wartosc {wartosc}.".format(nazwa='a', wartosc=a))
# nazwa = 'a'
# wartosc = a
# print(f"Zmienna {nazwa} ma wartosc {wartosc}.")
# print(f"Zmienna {(nazwa+'bcde').upper()} ma wartosc {1+1}.")

# # Przykady funkcji print
# print(1, 2, 3, sep="+", end="")
# print("=6")