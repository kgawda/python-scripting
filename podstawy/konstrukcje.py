# Dekorator

import functools

@functools.cache
def kwadrat(x):
    print("Licze kwadrat", x)
    return x ** 2

print(kwadrat(7))
print(kwadrat(7))
print(kwadrat(7))

# Context manager

with open("typy.py") as f:
    dlugosc = len(f.read())

# # Odpowiada to takiemu kawałkowi:
# f = open("typy.py")
# try:
#     dlugosc = len(f.read())
# finally:
#     f.close()

print("Plik typy.py ma dlugosc", dlugosc, "znaków")
