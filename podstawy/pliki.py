with open("example_utf8.txt", encoding="utf-8") as f:
    example_utf8 = f.read()

with open("example_cp1250.txt", encoding="cp1250") as f:
    example_cp1250 = f.read()

# "cp1250" domyślne na Windows
# "utf-8" domyślne na Linux/Mac

print(repr(example_utf8))
print(repr(example_cp1250))
#  print(example_utf8)  # wydrukuje wiele linji
lines = example_utf8.splitlines()  # opcjonalnie: keepends=True
print(lines)

with open("example_utf8.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()  # usuwa białe znaki z początku i końca stringa. rstrip() - tylko z końca
        if not line or line.startswith('#'):
            continue
        print(line)

# Pathlib
import pathlib
katalog = pathlib.Path(".")
assert katalog.exists()
assert katalog.is_dir()
assert not katalog.is_file()
for item in katalog.iterdir():
    print(repr(item), item.resolve())

print(list(katalog.glob('*.py')))  # wyszukiwanie po rozszerzeniu

p = pathlib.Path("C:/") / "podkatalog" / "plik.txt"
print(p)

#jak sobie radzić z \ w ścieżkach windows
"C:\\Windows\\"
r"C:\Windows"  # nie działa dla \ kończącego string
pathlib.Path("C:/Windows")
